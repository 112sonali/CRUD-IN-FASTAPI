from pydantic import BaseModel


class user(BaseModel):
    name:str
    email: str
    phone:str
    password:str


class Show(BaseModel):
    id:int

class Filter(BaseModel):
    name:str

class Update(BaseModel):
    id:int
    name:str
    email:str
    phone:str