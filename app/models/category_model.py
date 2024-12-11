from sqlalchemy import Column, Integer, String
from pydantic import BaseModel
from app.connection.database import Base

# Definição do modelo SQLAlchemy
class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

# Definição dos schemas Pydantic
class CategoryBase(BaseModel):
    name: str

class CategoryCreate(CategoryBase):
    pass

class CategoryResponse(CategoryBase):
    id: int