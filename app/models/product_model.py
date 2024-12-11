# app/models/product.py
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from pydantic import BaseModel
from app.connection.database import Base
from sqlalchemy.orm import relationship

from app.models.subcategory_model import SubCategoryResponse

# Definição do modelo SQLAlchemy
class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Float)
    sub_category_id = Column(Integer, ForeignKey("subcategories.id"))  # Chave estrangeira para SubCategory
    sub_category = relationship("SubCategory") #relationship("Category", lazy="joined")

# Definição dos schemas Pydantic
class ProductBase(BaseModel):
    name: str
    price: float
    sub_category_id: int

class ProductCreate(ProductBase):
    pass

class ProductResponse(ProductBase):
    id: int
    sub_category: SubCategoryResponse