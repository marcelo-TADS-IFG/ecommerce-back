# app/models/role_model.py
from sqlalchemy import Column, Integer, String
from pydantic import BaseModel
from app.connection.database import Base

# Definição do modelo SQLAlchemy para Role
class Role(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(String)

    def __repr__(self):
        return f"<Role(id={self.id}, name={self.name}, description={self.description})>"

# Definição do schema Pydantic para resposta de Role
class RoleResponse(BaseModel):
    id: int
    name: str
    description: str | None = None  # Descrição pode ser opcional

    class Config:
        orm_mode = True  # Permite que o Pydantic use o modelo ORM para serializar os dados

    # Definição do schema Pydantic para criação de Role
class RoleCreate(BaseModel):
    name: str
    description: str | None = None  # Descrição pode ser opcional

