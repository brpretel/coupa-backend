import sqlalchemy
from fastapi import HTTPException
from db import database
from models import user
from schemas.request.user_input_data import UserRole
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class MasterManager:

    @staticmethod
    async def update_role(user_id, new_role):
        try:
            # Update the user's role, search by user_id
            query = user.update().where(user.c.id == user_id).values(user_role=new_role)
            await database.execute(query)

            # Fetch the updated user data to return
            updated_user_query = sqlalchemy.select([user.c.id, user.c.username, user.c.user_role]).where(user.c.id == user_id)
            updated_user = await database.fetch_one(updated_user_query)
            return updated_user

        except Exception as e:
            error_message = f"Failed to update user role: {str(e)}, check if user exists"
            print(error_message)
            raise HTTPException(status_code=500, detail=error_message)

    @staticmethod
    async def update_status(user_id, new_status):
        try:
            # Update the user's status, search by user_id
            query = user.update().where(user.c.id == user_id).values(status=new_status)
            await database.execute(query)

            # Fetch the updated user data to return
            updated_user_query = sqlalchemy.select([user.c.id, user.c.username, user.c.status]).where(
                user.c.id == user_id)
            updated_user = await database.fetch_one(updated_user_query)
            return updated_user

        except Exception as e:
            error_message = f"Failed to update user status: {str(e)}, check if user exists"
            print(error_message)
            raise HTTPException(status_code=500, detail=error_message)

    """
    @staticmethod
    async def update_user(user_data):
        try:
            query = update(usuario).where(usuario.c.user_id == user_data["user_id"]).values(role=user_data["role"],
                                                                                            status=user_data["status"])
            await database.execute(query)
            return await database.fetch_one(usuario.select().where(usuario.c.user_id == user_data["user_id"]))
        except Exception as e:
            print("Error updating user: ", e)
    """

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
