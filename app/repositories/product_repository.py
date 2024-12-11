from app.models.product_model import Product, ProductCreate
from app.connection.database import database
from app.models.subcategory_model import SubCategory 
from sqlalchemy.orm import joinedload

class ProductRepository:
    
    def get_all(self):
        with database.get_session() as session:
            return session.query(Product).options(joinedload(Product.sub_category).joinedload(SubCategory.category)).all()

    def get_by_id(self, product_id: int):
        with database.get_session() as session:
            return session.query(Product).filter(Product.id == product_id).first()

    def create(self, product_data: ProductCreate):
        with database.get_session() as session:
            db_product = Product(
                name=product_data.name,
                price=product_data.price,
                sub_category_id=product_data.sub_category_id  # Associa o produto a uma subcategoria
            )
            session.add(db_product)
            session.commit()
            session.refresh(db_product)

             # Busca a subcategoria correspondente e retorna junto com o produto
            db_product = session.query(Product).options(joinedload(Product.sub_category).joinedload(SubCategory.category)).filter(Product.id == db_product.id).first()

            return db_product

    def delete(self, product_id: int):
        with database.get_session() as session:
            product = session.query(Product).filter(Product.id == product_id).first()
            if product:
                session.delete(product)
                session.commit()
                return True
            return False