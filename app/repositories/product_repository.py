# app/repositories/product_repository.py
from app.models.product_model import Product, ProductCreate
from app.connection.database import database

class ProductRepository:
    
    def get_all(self):
        with database.get_session() as session:
            return session.query(Product).all()

    def get_by_id(self, product_id: int):
        with database.get_session() as session:
            return session.query(Product).filter(Product.id == product_id).first()

    def create(self, product_data: ProductCreate):
        with database.get_session() as session:
            db_product = Product(
                name=product_data.name,
                price=product_data.price,
                #subcategory_id=product_data.subcategory_id  # Associando a subcategoria
            )
            session.add(db_product)
            session.commit()
            session.refresh(db_product)
            return db_product

    def delete(self, product_id: int):
        with database.get_session() as session:
            product = session.query(Product).filter(Product.id == product_id).first()
            if product:
                session.delete(product)
                session.commit()
                return True
            return False
        
    def get_by_subcategory(self, subcategory_id: int):
        with database.get_session() as session:
            return session.query(Product).filter(Product.subcategory_id == subcategory_id).all()  # Novo método
