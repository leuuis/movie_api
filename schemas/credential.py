
from pydantic import BaseModel

class Credential(BaseModel):
    user: str
    password: str

    class Config:
        schema_extra = {
            "example":{
                "user": "my_email@gmail.com",
                "password": "m1P@ssw0rd"
            }
        }