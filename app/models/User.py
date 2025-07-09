# import json
# from pathlib import Path
#
# data_path = Path(__file__).resolve().parent.parent / "data" / "users.json"
#
# with data_path.open(encoding="utf-8") as f:
#     users_data = json.load(f)
#
# users_data = [
#     {"id": i, "email": f"user{i}@example.com", "first_name": f"User{i}", "last_name": f"Test"}
#     for i in range(1, 21)
# ]


from pydantic import BaseModel, EmailStr, HttpUrl
from sqlmodel import Field, SQLModel


class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    email: EmailStr
    first_name: str
    last_name: str
    avatar: str


class UserCreate(BaseModel):
    email: EmailStr
    first_name: str
    last_name: str
    avatar: HttpUrl


class UserUpdate(BaseModel):
    email: EmailStr | None = None
    first_name: str | None = None
    last_name: str | None = None
    avatar: HttpUrl | None = None
