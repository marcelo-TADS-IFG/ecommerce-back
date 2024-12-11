from fastapi import Request
from fastapi.responses import JSONResponse
from app.repositories.user_repository import UserRepository
from app.models.user_model import UserCreate, UserLogin
from app.utils.settings import settings
from jose import jwt

class UserService:

    def __init__(self):
        self.repository = UserRepository()  # Instância do repositório de usuários

    def login(self, user: UserLogin, req: Request):
        # Busca o usuário pelo nome de usuário no banco de dados
        user_db = self.get_user_by_username(username=user.username)

        # Verifica se o usuário existe e se a senha está correta
        if not user_db or user_db.password != user.password:
            return JSONResponse(
                status_code=401,
                content="usuário não encontrado!",
            )
        
        # Cria o payload para o token JWT
        payload = {
            "username": user_db.username,
            "user_id": user_db.id,
        }

        # Gera o token JWT
        access_token = jwt.encode(payload, settings.jwt_key, settings.jwt_algorithm)

        return access_token

    # Retorna todos os usuários
    def get_all_users(self):
        return self.repository.get_all()

    # Retorna um usuário pelo ID
    def get_user_by_id(self, user_id: int):
        return self.repository.get_by_id(user_id)
   
    # Retorna um usuário pelo nome de usuário
    def get_user_by_username(self, username: int):
        return self.repository.get_by_username(username)

    # Cria um novo usuário
    def create_user(self, user: UserCreate):
        return self.repository.create(user)

    # Remove um usuário pelo ID
    def delete_user(self, user_id: int):
        return self.repository.delete(user_id)
