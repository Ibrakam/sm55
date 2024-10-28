from fastapi import FastAPI, Request
from api.user_api.users import user_router
from database import Base, engine
from api.post_api.posts import post_router

Base.metadata.create_all(engine)
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

templates = Jinja2Templates(directory="templates")

app = FastAPI(docs_url="/docs")

app.include_router(user_router)
app.include_router(post_router)


@app.get("/", response_class=HTMLResponse)
async def main(request: Request):
    return templates.TemplateResponse(name="index.html", request=request)
