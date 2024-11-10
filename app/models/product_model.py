# app/models/product.py
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from pydantic import BaseModel
from app.connection.database import Base

# Definição do modelo SQLAlchemy
class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Float)
    # subcategory_id = Column(Integer, ForeignKey('subcategories.id'))  # Relacionamento com Subcategory

    # subcategory = relationship("Subcategory", back_populates="products")

# Definição dos schemas Pydantic
class ProductBase(BaseModel):
    name: str
    price: float
    # subcategory_id: int  # ID da subcategoria associada

class ProductCreate(ProductBase):
    pass

class ProductResponse(ProductBase):
    id: int

    class Config:
        orm_mode = True
