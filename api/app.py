from fastapi import FastAPI
from api.controllers import main_router

app = FastAPI()

app.include_router(main_router, prefix="/api")
