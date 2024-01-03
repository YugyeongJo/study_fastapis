from fastapi import APIRouter
router = APIRouter()

from starlette.responses import HTMLResponse

from fastapi.templating import Jinja2Templates
from fastapi import Request

# html 틀이 있는 폴더 위치
templates = Jinja2Templates(directory="templates/")

# 회원 가입 form   /users/form  > users/inserts.html
@router.get("/form")
async def insert(request:Request):
    pass
    return templates.TemplateResponse(name="users/inserts.html",context = {"request": request})

# 회원 가입 /users/inserts > 가입이 완료되면 로그인으로 이동 users/login.html
@router.get("/insert")
async def insert(request:Request):
    pass    #bisness는 여기(실제 들어오는 곳과 나가는 곳이 다른 곳)
    return templates.TemplateResponse(name="users/login.html",context = {"request": request})