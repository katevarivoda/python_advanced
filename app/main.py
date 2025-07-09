from contextlib import asynccontextmanager

from dotenv import load_dotenv
load_dotenv()

import uvicorn

from app.database.engine import create_db_and_tables


from fastapi_pagination import add_pagination

from fastapi import FastAPI

from app.routers import users, health

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting application...")
    create_db_and_tables()
    yield
    print("Shutting down application...")


app = FastAPI(title="Reqres Clone", lifespan=lifespan)

app.include_router(users.router, prefix="/api")

app.include_router(health.router, prefix="/api")

add_pagination(app)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8002)
