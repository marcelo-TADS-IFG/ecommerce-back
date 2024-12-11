from fastapi import APIRouter, HTTPException
from app.services.role_service import RoleService
from app.models.role_model import RoleResponse, RoleCreate

router = APIRouter()
service = RoleService()

@router.get("/roles", response_model=list[RoleResponse])
def get_all_roles():
    """
    Retorna todas as roles.
    """
    return service.get_all_roles()

@router.get("/role/{role_id}", response_model=RoleResponse)
def get_role_by_id(role_id: int):
    """
    Retorna uma role pelo ID.
    """
    role = service.get_role_by_id(role_id)
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")
    return role

@router.post("/role/save", response_model=RoleResponse)
def create_role(role: RoleCreate):
    """
    Cria uma nova role.
    """
    return service.create_role(role)

@router.delete("/role/{role_id}")
def delete_role(role_id: int):
    """
    Deleta uma role pelo ID.
    """
    deleted = service.delete_role(role_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Role not found")
    return {"message": "Role deleted successfully"}
