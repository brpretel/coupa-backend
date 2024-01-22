import sqlalchemy
from fastapi import HTTPException
from db import database
from managers.auth import AuthManager
from models import case, vertical
from models.enums import UserRole
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class MasterManager:

    @staticmethod
    async def register_master(password, user_data):
        user_data["user_role"] = UserRole.master
        if password == "coupaadmin123456":
            return await AuthManager.register(user_data)
        else:
            raise HTTPException(400, "invalid token")

    @staticmethod
    async def create_case(product_data):
        try:
            id_ = await database.execute(case.insert().values(product_data))
        except:
            return None
        return await database.fetch_one(case.select().where(case.c.id == id_))

    @staticmethod
    async def get_verticals():
        try:
            # Search all verticals
            query = sqlalchemy.select([vertical])
            result = await database.fetch_all(query)
            return result
        except Exception as e:
            error_message = f"Failed to get verticals: {str(e)}"
            print(error_message)
            raise HTTPException(status_code=500, detail=error_message)

    @staticmethod
    async def create_vertical(vertical_name):
        try:
            # Check if vertical exists
            check_query = sqlalchemy.select([vertical]).where(vertical.c.vertical_name == vertical_name)
            existing_vertical = await database.fetch_one(check_query)
            if existing_vertical:
                raise HTTPException(status_code=400, detail="Vertical already exists")

            # Insert new vertical
            query = sqlalchemy.insert(vertical).values(vertical_name=vertical_name)
            vertical_id = await database.execute(query)

            # Returns created vertical
            select_query = sqlalchemy.select([vertical]).where(vertical.c.id == vertical_id)
            new_vertical = await database.fetch_one(select_query)
            return new_vertical

        except HTTPException as http_exc:
            raise http_exc
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Failed to create vertical: {str(e)}")

    @staticmethod
    async def update_vertical(vertical_id, vertical_name):
        try:
            # Check if vertical exists by ID
            check_query = sqlalchemy.select([vertical]).where(vertical.c.id == vertical_id)
            check_result = await database.fetch_one(check_query)
            if check_result is None:
                raise HTTPException(status_code=404, detail="Vertical not found")

            # Updates Vertical Name
            update_query = sqlalchemy.update(vertical).where(vertical.c.id == vertical_id).values(
                vertical_name=vertical_name)
            await database.execute(update_query)

            # Returns updated vertical
            updated_vertical_query = sqlalchemy.select([vertical]).where(vertical.c.id == vertical_id)
            updated_vertical = await database.fetch_one(updated_vertical_query)
            return updated_vertical

        except HTTPException as http_exc:
            raise http_exc
        except Exception as e:
            error_message = f"Failed to update vertical: {str(e)}"
            raise HTTPException(status_code=500, detail=error_message)

    @staticmethod
    async def delete_vertical(vertical_id):
        try:
            # Check if vertical exists by ID
            check_query = sqlalchemy.select([vertical]).where(vertical.c.id == vertical_id)
            check_result = await database.fetch_one(check_query)
            if check_result is None:
                raise HTTPException(status_code=404, detail="Vertical not found")

            # Delete Vertical
            delete_query = sqlalchemy.delete(vertical).where(vertical.c.id == vertical_id)
            await database.execute(delete_query)

            return {"message": "Vertical deleted successfully", "vertical_id": vertical_id}

        except HTTPException as http_exc:
            raise http_exc
        except Exception as e:
            error_message = f"Failed to delete vertical: {str(e)}"
            print(error_message)
            raise HTTPException(status_code=500, detail=error_message)

    """Need to generate method to CREATE, UPDATE AND DELETE
    user_vertical options, needs to write in DB table"""
    """@staticmethod
    async def create_user_vertical(vertical_data):
        id_ = await database.execute(dias.insert().values(dias_data))
        return await database.fetch_one(dias.select().where(dias.c.id == id_))"""

    # Guide Methods for new CRUD

    """@staticmethod
    async def post_product_for_user(product_data):
        product_exists = await database.fetch_one(
            producto.select().where(producto.c.id == product_data["producto"])
        )
        user_exists = await database.fetch_one(
            usuario.select().where(usuario.c.id == product_data["usuario"])
        )
        if product_exists and user_exists:
            id_ = await database.execute(disp_usuario_producto.insert().values(product_data))
            return await database.fetch_one(
                disp_usuario_producto.select().where(disp_usuario_producto.c.id == id_))
        else:
            return None

    
    @staticmethod
    async def create_dia_for_distribuidor(dia_data):
        dia_exists = await database.fetch_one(
            dias.select().where(dias.c.id == dia_data["dia"])
        )

        user_exists = await database.fetch_one(
            usuario.select().where(usuario.c.id == dia_data["usuario"])
        )
        if dia_exists and user_exists:
            id_ = await database.execute(disp_dias_de_distribuidor.insert().values(dia_data))
            return await database.fetch_one(
                disp_dias_de_distribuidor.select().where(disp_dias_de_distribuidor.c.id == id_))
        else:
            return None

    @staticmethod
    async def get_all_users():
        q1 = usuario.select()
        users = await database.fetch_all(q1)
        return users

    @staticmethod
    async def get_all_products():
        q1 = producto.select()
        productos = await database.fetch_all(q1)
        return productos

    @staticmethod
    async def get_user_for_update(user_id):
        q1 = usuario.select().where(usuario.c.id == user_id)
        q2 = dias.select().where(~dias.c.id.in_(select([disp_dias_de_distribuidor.c.dia]).where(disp_dias_de_distribuidor.c.usuario == user_id))).order_by(sqlalchemy.asc(dias.c.fecha))
        q3 = producto.select().where(~producto.c.id.in_(select([disp_usuario_producto.c.producto]).where(disp_usuario_producto.c.usuario == user_id)))
        user = await database.fetch_one(q1)
        dias_semana = await database.fetch_all(q2)
        productos = await database.fetch_all(q3)
        return user, dias_semana, productos

    @staticmethod
    async def update_user(user_data):
        try:
            query = update(usuario).where(usuario.c.user_id == user_data["user_id"]).values(role=user_data["role"],
                                                                                            status=user_data["status"])
            await database.execute(query)
            return await database.fetch_one(usuario.select().where(usuario.c.user_id == user_data["user_id"]))
        except Exception as e:
            print("Error updating user: ", e)

    @staticmethod
    async def get_user_products_and_days(user_id):
        days_query = (
            select([dias.c.dia])
            .select_from(disp_dias_de_distribuidor.join(dias))
            .where(disp_dias_de_distribuidor.c.usuario == user_id)
        )
        days = await database.fetch_all(days_query)
        products_query = (
            select([producto.c.nombre, producto.c.categoria])
            .select_from(disp_usuario_producto.join(producto))
            .where(disp_usuario_producto.c.usuario == user_id)
        )
        products = await database.fetch_all(products_query)
        return days, products"""
