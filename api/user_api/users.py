from fastapi import APIRouter
from database.userservice import (register_user_db, get_exact_user_db, get_all_users_db,
                                  update_user_db, delete_user_db)
from pydantic import BaseModel
from typing import Optional
import re

user_router = APIRouter(prefix="/user", tags=["Пользователи"])

regex = re.compile(r"^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$")


def check_email(email):
    if re.fullmatch(regex, email):
        return True
    return False


class User(BaseModel):
    username: str
    phone_number: str
    password: str
    email: str
    user_city: Optional[str] = None
    birthday: Optional[str] = None


@user_router.post("/register_user")
async def register_user_api(user_data: User):
    user_db = dict(user_data)
    mail_validation = check_email(user_data.email)
    if mail_validation:
        result = register_user_db(**user_db)
        return {"status": 1, "message": "Пользовтель успешно добавлен"}
    return {"status": 0, "message": "Неправильный email"}


@user_router.get("/get_exact_user")
async def get_exact_user_api(user_id: int):
    result = get_exact_user_db(user_id)
    return result


@user_router.get("/get_all_users")
async def get_all_users_api():
    return get_all_users_db()


@user_router.put("/update_user_info")
async def update_user_api(user_id: int, change_info: str, new_info: str):
    result = update_user_db(user_id, change_info, new_info)
    if result:
        return "Данные успешно изменены"
    return result


@user_router.delete("/delete_user")
async def delete_user_api(user_id: int):
    return delete_user_db(user_id)
