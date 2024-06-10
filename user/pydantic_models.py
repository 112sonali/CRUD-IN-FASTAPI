from pydantic import BaseModel


class user(BaseModel):
    name:str
    email: str
    phone:str
    password:str