from jwt import encode, decode

def create_jwt(data: dict) -> str :
    token: str =  encode(payload=data, algorithm="HS256", key="my_secret_key")
    return token

def decode_jwt(token: str) -> dict :
    data = decode(jwt=token, algorithms=['HS256'], key="my_secret_key")
    return data