from fastapi import APIRouter
router = APIRouter()

from starlette.responses import HTMLResponse

from fastapi.templating import Jinja2Templates
from fastapi import Request

# html 틀이 있는 폴더 위치
templates = Jinja2Templates(directory="templates/")

# 회원 가입 / users/inserts
@router.get("/insert")
async def insert(request:Request):
    pass
    return templates.TemplateResponse(name="users/inserts.html",context = {"request": request})