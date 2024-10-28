from fastapi import APIRouter
from database.postservice import *

post_router = APIRouter(prefix="/post", tags=["Пост", "Коммент", "Хэштег"])


@post_router.get("/get_all_post")
async def get_all():
    return get_all_users_posts_db()


@post_router.post("/add_user_post")
async def add_post_api(user_id: int, main_text: str, hashtags: str = None):
    result = register_user_post_db(user_id, main_text, hashtags)
    return result



@post_router.get("/get-all-users-comment")
async def get_all_users_comments_api(user_id: int):
    return all_user_coment_db(user_id)


@post_router.get("/update-comment")
async def update_comment_api(comment_id: int, new_info: str):
    result = update_coment_db(comment_id, new_info)
    if result:
        return "Публикация успешна изменена"
    return result
