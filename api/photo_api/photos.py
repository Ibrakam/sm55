# from fastapi import APIRouter, UploadFile, File
# import random
#
# from database.postservice import add_post_photo
#
# photo_router = APIRouter(prefix="/photo", tags=["Фотографии"])
#
#
# @photo_router.post("/add_photo")
# async def add_photo_api(post_id: int, photo_file: UploadFile = File(...)):
#     file_id = random.randint(1, 10000000)
#     if photo_file:
#         with open(f"database/photo/photo_{file_id}_{post_id}.jpg",
#                   "wb") as photo:
#             photo_to_save = await photo_file.read()
#             photo.write(photo_to_save)
#             add_post_photo(post_id, photo)
#             return {"status": 1, "message": "Успешно загружено"}
#     return {"status": 0, "message": "Ошибка"}
