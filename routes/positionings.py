from fastapi import APIRouter
router = APIRouter()

from starlette.responses import HTMLResponse

from fastapi.templating import Jinja2Templates
from fastapi import Request

# html 틀이 있는 폴더 위치
templates = Jinja2Templates(directory="templates/")

@router.get("/buttons")
async def form(request:Request):
    pass
    return templates.TemplateResponse(name="positionings/buttons.html",context = {"request": request})

@router.get("/cards")
async def form(request:Request):
    pass
    return templates.TemplateResponse(name="positionings/cards.html",context = {"request": request})

@router.get("/colors")
async def form(request:Request):
    pass
    return templates.TemplateResponse(name="positionings/colors.html",context = {"request": request})

@router.get("/containers")
async def form(request:Request):
    pass
    return templates.TemplateResponse(name="positionings/containers.html",context = {"request": request})