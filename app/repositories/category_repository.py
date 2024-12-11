from app.models.category_model import Category, CategoryCreate
from app.connection.database import database  # Importe a instância do banco

class CategoryRepository:
    
    def get_all(self):
        with database.get_session() as session:
            return session.query(Category).all()

    def get_by_id(self, category_id: int):
        with database.get_session() as session:
            return session.query(Category).filter(Category.id == category_id).first()

    def create(self, category_data: CategoryCreate):
        with database.get_session() as session:
            db_category = Category(name=category_data.name)
            session.add(db_category)
            session.commit()
            session.refresh(db_category)
            return db_category

    def delete(self, category_id: int):
        
        with database.get_session() as session:
            category = session.query(Category).filter(Category.id == category_id).first()
            if category:
                session.delete(category)
                session.commit()
                return True
            return False