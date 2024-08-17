from fastapi import status
from fastapi import APIRouter
from utils.jwt_manager import create_jwt
from schemas.credential import Credential
from fastapi.responses import JSONResponse

auth_router =  APIRouter()

@auth_router.post('/login', tags=['Auth'])
def login(credential: Credential):
    if credential.user == "admin@gmail.com" and credential.password == "admin":
        token: str = create_jwt(credential.model_dump())
    return JSONResponse(content=token, status_code=status.HTTP_200_OK)
