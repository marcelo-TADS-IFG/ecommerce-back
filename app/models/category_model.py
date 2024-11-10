from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from pydantic import BaseModel
from app.connection.database import Base

# Modelo da entidade Category
class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)

    # Relacionamento um-para-muitos com SubCategory
    # subcategories = relationship("SubCategory", back_populates="category")

class CategoryBase(BaseModel):
    name: str

class CategoryCreate(CategoryBase):
    pass

class CategoryResponse(CategoryBase):
    id: int
    #subcategories: list["SubCategoryResponse"] = []