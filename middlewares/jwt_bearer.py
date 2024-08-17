

from fastapi.security import HTTPBearer
from utils.jwt_manager import decode_jwt
from fastapi import HTTPException, Request

class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        data = decode_jwt(auth.credentials)
        if data['user'] != "admin@gmail.com":
            raise HTTPException(status_code=403, detail="Credenciales invalidas")