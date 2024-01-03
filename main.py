from fastapi import FastAPI
app = FastAPI()

from routes.homes import router as event_router
app.include_router(event_router, prefix='/home') #주소창 
                        
from routes.gadgets import router as gadgets_router
app.include_router(gadgets_router, prefix='/gadgets') #gadgets 주소에 있는 하위항목들 모두 연결
from routes.positionings import router as positionings_router
app.include_router(positionings_router, prefix='/positionings') #positionings 주소에 있는 하위항목들 모두 연결
from routes.users import router as users_router #users 주소에 있는 하위항목들 모두 연결
app.include_router(users_router, prefix='/users')

#다른언어를 사용해서 유지보수를 해야할 경우 오류를 막기 위해
from fastapi import Request
from fastapi.templating import Jinja2Templates

# html 틀이 있는 폴더 위치
templates = Jinja2Templates(directory="templates/")

@app.get("/")                                                                
async def root(request:Request):                                             
    return templates.TemplateResponse("main.html"
                                      ,{'request': request})
    
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 실제 운영 환경에서는 접근 가능한 도메인만 허용하는 것이 좋습니다.
    allow_methods=["*"],
    allow_headers=["*"],
)