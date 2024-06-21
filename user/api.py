from fastapi import APIRouter
from . models import *
from . pydantic_models import user,Show,Filter,Update
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
    
     
@app.get("/show_data/")
async def show_all():
     user_obj = await Persone.all()
     return user_obj

@app.post("/show_user_data/")
async def show_user(data:Show):
     user_obj = await Persone.get(id=data.id)
     return user_obj

@app.post("/filter_data/")
async def show_data(data:Filter):
     user_obj = await Persone.filter(name=data.name)
     return user_obj

@app.delete("/delete_user/")
async def delete_user(data:Show):
     user_obj = await Persone.get(id=data.id).delete()
     return user_obj

@app.put("/update_user/")
async def update_user(data:Update):
     user_obj = await Persone.get(id=data.id)
     new = await Persone.filter(id=data.id).update(name=data.name,email=data.email,
                                                  phone=data.phone,)
     return new
     

