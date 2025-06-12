from fastapi_pagination import add_pagination

from fastapi import FastAPI
from app.routers import users

app = FastAPI(title="Reqres Clone")

app.include_router(users.router, prefix="/api")

@app.get("/")
def root():
    return {"message": "FastAPI сервис запущен!"}

@app.get("/status")
def get_status():
    return {"status": "ok"}

@app.get("/debug")
def debug():
    return {"message": "this is debug"}

add_pagination(app)