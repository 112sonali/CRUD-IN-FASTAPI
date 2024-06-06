from fastapi import FastAPI
from user import api as UserRouter

app = FastAPI()

app.include_router(UserRouter.app,tags=["API"])