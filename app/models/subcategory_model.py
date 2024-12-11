# app/models/subcategory.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from pydantic import BaseModel
from app.connection.database import Base
from app.models.category_model import CategoryResponse

# Definição do modelo SQLAlchemy
class SubCategory(Base):
    __tablename__ = "subcategories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    category_id = Column(Integer, ForeignKey("categories.id"))  # Chave estrangeira para Category
    category = relationship("Category")

# Definição dos schemas Pydantic
class SubCategoryBase(BaseModel):
    name: str
    category_id: int

class SubCategoryCreate(SubCategoryBase):
    pass

class SubCategoryResponse(SubCategoryBase):
    id: int
    category: CategoryResponse