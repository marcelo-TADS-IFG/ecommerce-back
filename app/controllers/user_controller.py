# app/controllers/user_controller.py
from fastapi import APIRouter, HTTPException, Request
from app.services.user_service import UserService
from app.models.user_model import UserLogin, UserResponse, UserCreate

router = APIRouter()
service = UserService()

@router.post("/user/login", response_model=str)
def login(user: UserLogin, req: Request):
    dados_autenticacao = service.login(user=user, req=req)
    return dados_autenticacao

@router.get("/users", response_model=list[UserResponse])
def get_all_users():
    return service.get_all_users()

@router.get("/user/{user_id}", response_model=UserResponse)
def get_user_by_id(user_id: int):
    user = service.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.post("/user/save", response_model=UserResponse)
def create_user(user: UserCreate):
    return service.create_user(user)

@router.delete("/user/{user_id}")
def delete_user(user_id: int):
    deleted = service.delete_user(user_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted successfully"}