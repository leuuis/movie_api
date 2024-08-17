from fastapi import APIRouter
from fastapi.responses import HTMLResponse

home_router = APIRouter()

@home_router.get('/', tags=['Home'])
def message():
    return HTMLResponse('<h1> I\'m still alive from GT502 </h1>')