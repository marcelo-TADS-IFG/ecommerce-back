# app/services/subcategory_service.py
from app.repositories.subcategory_repository import SubCategoryRepository
from app.models.subcategory_model import SubCategoryCreate

class SubcategoryService:
    def __init__(self):
        self.repository = SubCategoryRepository()

    def get_all_subcategories(self):
        return self.repository.get_all()

    def get_subcategory_by_id(self, subcategory_id: int):
        return self.repository.get_by_id(subcategory_id)

    def create_subcategory(self, subcategory: SubCategoryCreate):
        return self.repository.create(subcategory)

    def delete_subcategory(self, subcategory_id: int):
        return self.repository.delete(subcategory_id)
