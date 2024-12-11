# app/controllers/subcategory_controller.py
from fastapi import APIRouter, HTTPException
from app.services.subcategory_service import SubcategoryService
from app.models.subcategory_model import SubCategoryResponse, SubCategoryCreate

router = APIRouter()
service = SubcategoryService()

@router.get("/subcategories", response_model=list[SubCategoryResponse])
def get_all_subcategories():
    return service.get_all_subcategories()

@router.get("/subcategory/{subcategory_id}", response_model=SubCategoryResponse)
def get_subcategory_by_id(subcategory_id: int):
    subcategory = service.get_subcategory_by_id(subcategory_id)
    if not subcategory:
        raise HTTPException(status_code=404, detail="Subcategory not found")
    return subcategory

@router.post("/subcategory/save", response_model=SubCategoryResponse)
def create_subcategory(subcategory: SubCategoryCreate):
    return service.create_subcategory(subcategory)

@router.delete("/subcategory/{subcategory_id}")
def delete_subcategory(subcategory_id: int):
    deleted = service.delete_subcategory(subcategory_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Subcategory not found")
    return {"message": "Subcategory deleted successfully"}
