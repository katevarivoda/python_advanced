from fastapi import FastAPI
from app.routers import users

app = FastAPI(title="Reqres Clone")
app.include_router(users.router, prefix="/api")

@app.get("/")
def root():
    return {"message": "FastAPI сервис запущен!"}