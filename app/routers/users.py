from fastapi import APIRouter, HTTPException
from app.models.user import users_data

router = APIRouter()

@router.get("/users/{user_id}")
def get_user(user_id: int):
    user = next((u for u in users_data if u["id"] == user_id), None)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"data": user}
