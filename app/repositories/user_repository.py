# app/repositories/user_repository.py

from app.models.role_model import Role
from app.models.user_model import User, UserCreate
from app.connection.database import database  
from sqlalchemy.orm import joinedload

class UserRepository:
   
    def get_all(self):
        with database.get_session() as session:
            # Usa `joinedload` para carregar o relacionamento `Role` de forma eficiente
            return session.query(User).options(joinedload(User.role)).all()

    def  get_by_id(self, user_id: int):
        with database.get_session() as session:
            return session.query(User).filter(User.id == user_id).first()
       
   
    def get_by_username(self, username: int):
        with database.get_session() as session:
            return session.query(User).filter(User.username == username).first()

    def create(self, user_data: UserCreate):
        with database.get_session() as session:
            # Cria um novo User
            db_user = User(
                name=user_data.name,
                username=user_data.username,
                password=user_data.password,
                role_id=user_data.role_id  # Associa a role com o usuário
            )
            session.add(db_user)
            session.commit()
            session.refresh(db_user)

            # Busca a role correspondente e retorna junto com o usuário
            db_role = session.query(Role).filter(Role.id == db_user.role_id).first()
            db_user.role = db_role  # Atribui a role ao objeto da user

            return db_user
         
    def delete(self, user_id: int):
        with database.get_session() as session:
            user = session.query(User).filter(User.id == user_id).first()
            if user:
                session.delete(user)
                session.commit()
                return True
            return False