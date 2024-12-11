from app.repositories.category_repository import CategoryRepository
from app.models.category_model import CategoryCreate

class CategoryService:
    def __init__(self):
        self.repository = CategoryRepository()  # Instância do repositório

    # Retorna todas as categorias
    def get_all_categories(self):
       return self.repository.get_all()

    # Retorna uma categoria pelo ID
    def get_category_by_id(self, category_id: int):
        return self.repository.get_by_id(category_id)

    # Cria uma nova categoria
    def create_category(self, category: CategoryCreate):
        return self.repository.create(category)

    # Remove uma categoria pelo ID
    def delete_category(self, category_id: int):
        return self.repository.delete(category_id)
