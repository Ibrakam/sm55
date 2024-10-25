from fastapi import FastAPI
from api.photo_api.photos import photo_router
from api.user_api.users import user_router
from database import Base, engine
Base.metadata.create_all(engine)

app = FastAPI(docs_url="/")

app.include_router(photo_router)
app.include_router(user_router)
