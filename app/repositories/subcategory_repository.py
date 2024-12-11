from app.models.subcategory_model import SubCategory, SubCategoryCreate
from app.models.category_model import Category  # Importe o modelo de categoria
from app.connection.database import database  # Importe a instância do banco
from sqlalchemy.orm import joinedload

class SubCategoryRepository:
    
    def get_all(self):
        with database.get_session() as session:
            # Usa `joinedload` para carregar o relacionamento `Category` de forma eficiente
            return session.query(SubCategory).options(joinedload(SubCategory.category)).all()

    def get_by_id(self, subcategory_id: int):
        with database.get_session() as session:
            return session.query(SubCategory).filter(SubCategory.id == subcategory_id).first()

    def create(self, subcategory_data: SubCategoryCreate):
        with database.get_session() as session:
            # Cria a nova subcategoria
            db_subcategory = SubCategory(
                name=subcategory_data.name,
                category_id=subcategory_data.category_id  # Associa a subcategoria a uma categoria existente
            )
            session.add(db_subcategory)
            session.commit()
            session.refresh(db_subcategory)

            # Busca a categoria correspondente e retorna junto com a subcategoria
            db_category = session.query(Category).filter(Category.id == db_subcategory.category_id).first()
            db_subcategory.category = db_category  # Atribui a categoria ao objeto da subcategoria

            return db_subcategory
          
    def delete(self, subcategory_id: int):
        with database.get_session() as session:
            subcategory = session.query(SubCategory).filter(SubCategory.id == subcategory_id).first()
            if subcategory:
                session.delete(subcategory)
                session.commit()
                return True
            return False