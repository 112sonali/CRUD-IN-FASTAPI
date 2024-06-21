from fastapi import FastAPI
from user import api as UserRouter
from tortoise.contrib.fastapi import register_tortoise
from user import router as apirouter


app = FastAPI()

app.include_router(UserRouter.app)
app.include_router(apirouter.router)



register_tortoise(
    app,
    db_url="postgres://postgres:12345@127.0.0.1/crudfastapi",
    modules={'models': ['user.models',]},
    generate_schemas=True,
    add_exception_handlers=True
)
