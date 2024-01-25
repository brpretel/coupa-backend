import sqlalchemy
from fastapi import HTTPException
from db import database
from models import case, user
from passlib.context import CryptContext
from datetime import date

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class CasesManager:

    @staticmethod
    async def get_all_cases():
        try:
            query = sqlalchemy.select([case])
            result = await database.fetch_all(query)
            return result
        except Exception as e:
            error_message = f"Failed to get cases: {str(e)}"
            print(error_message)
            raise HTTPException(status_code=500, detail=error_message)

    @staticmethod
    async def create_case(case_data, current_user):
        try:
            user_id = current_user["id"]
            user_query = sqlalchemy.select([user.c.user_vertical]).where(user.c.id == user_id)
            user_vertical_result = await database.fetch_one(user_query)
            if user_vertical_result:
                user_vertical = user_vertical_result['user_vertical']
            else:
                return None

            case_data_dict = case_data.dict()
            case_data_dict["user_id"] = user_id
            case_data_dict["case_vertical"] = user_vertical
            case_data_dict["creation_date"] = date.today()
            query = case.insert().values(**case_data_dict)
            last_record_id = await database.execute(query)
            return {**case_data_dict, "id": last_record_id}

        except Exception as e:
            error_message = f"Failed to create case: {str(e)}"
            print(error_message)
            raise HTTPException(status_code=500, detail=error_message)

    @staticmethod
    async def update_case(case_id, case_data):
        try:
            query = case.update().where(case.c.id == case_id).values(**case_data.dict())
            await database.execute(query)
            return {**case_data.dict(), "id": case_id}
        except Exception as e:
            error_message = f"Failed to update case: {str(e)}"
            print(error_message)
            raise HTTPException(status_code=500, detail=error_message)

    @staticmethod
    async def delete_case(case_id):
        try:
            query = case.delete().where(case.c.id == case_id)
            await database.execute(query)
            return {"message": "Case deleted successfully"}
        except Exception as e:
            error_message = f"Failed to delete case: {str(e)}"
            print(error_message)
            raise HTTPException(status_code=500, detail=error_message)

    @staticmethod
    async def get_agent_case(current_user):
        try:
            query = sqlalchemy.select([case]).where(case.c.user_id == current_user["id"])
            result = await database.fetch_all(query)
            return result
        except Exception as e:
            error_message = f"Failed to get cases for agent {current_user['id']}: {str(e)}"
            print(error_message)
            raise HTTPException(status_code=500, detail=error_message)