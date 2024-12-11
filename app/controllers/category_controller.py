from fastapi import APIRouter, HTTPException
from app.services.category_service import CategoryService
from app.models.category_model import CategoryResponse, CategoryCreate

router = APIRouter()
service = CategoryService()

@router.get("/categories", response_model=list[CategoryResponse])
def get_all_categories():
    return service.get_all_categories()

@router.get("/category/{category_id}", response_model=CategoryResponse)
def get_category_by_id(category_id: int):
    category = service.get_category_by_id(category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category

@router.post("/category/save", response_model=CategoryResponse)
def create_category(category: CategoryCreate):
    return service.create_category(category)

@router.delete("/category/{category_id}")
def delete_category(category_id: int):
    deleted = service.delete_category(category_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Category not found")
    return {"message": "Category deleted successfully"}
