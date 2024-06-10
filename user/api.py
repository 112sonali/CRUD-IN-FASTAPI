from fastapi import APIRouter
from . models import *
from . pydantic_models import user
from passlib .context import CryptContext


app = APIRouter()
pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


def verify_password(plain_password, hashed_password):
        return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
        return pwd_context.hash(password)


@app.post("/")
async def create_user(data:user):
    if await Persone.exists(email=data.email):
        return {"status":False, "message":"Email Already Exists"}

    elif await Persone.exists(phone=data.phone):
        return {"status":False, "message":"Phone Number Already Exists"}
    
    else:
       user_obj = await Persone.create(name=data.name,email=data.email,
                                       phone=data.phone,
                                       password=get_password_hash(data.password))
       return user_obj