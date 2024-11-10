from sqlalchemy.orm import joinedload
from app.models.category_model import Category, CategoryCreate
from app.connection.database import database

class CategoryRepository:

    def get_all(self):
        with database.get_session() as session:
            # Retorna todas as categorias, incluindo subcategorias
            return session.query(Category).all()

    def get_by_id(self, category_id: int):
        with database.get_session() as session:
            # Retorna uma categoria específica com suas subcategorias
            return session.query(Category).filter(Category.id == category_id).first()

    def create(self, category_data: CategoryCreate):
        with database.get_session() as session:
            db_category = Category(name=category_data.name)
            session.add(db_category)
            session.commit()
            session.refresh(db_category)
            return db_category