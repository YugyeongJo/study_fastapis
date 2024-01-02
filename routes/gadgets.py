from fastapi import APIRouter
router = APIRouter()

#html파일을 html파일로 읽기 위한 모듈
from starlette.responses import HTMLResponse

from fastapi.templating import Jinja2Templates
from fastapi import Request

# html 틀이 있는 폴더 위치
templates = Jinja2Templates(directory="templates/")

@router.get("/forms")
async def form(request:Request):
    pass
    return templates.TemplateResponse(name="gadgets/forms.html",context = {"request": request})

@router.get("/grids")
async def form(request:Request):
    pass
    return templates.TemplateResponse(name="gadgets/grids.html",context = {"request": request})

@router.get("/standard")
async def form(request:Request):
    pass
    return templates.TemplateResponse(name="gadgets/standard.html",context = {"request": request})

@router.get("/tables")
async def form(request:Request):
    pass
    return templates.TemplateResponse(name="gadgets/tables.html",context = {"request": request})