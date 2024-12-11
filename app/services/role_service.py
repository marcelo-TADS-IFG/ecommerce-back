from app.repositories.role_repository import RoleRepository
from app.models.role_model import RoleCreate

class RoleService:
    def __init__(self):
        self.repository = RoleRepository()  # Instância do repositório

    # Retorna todas as roles
    def get_all_roles(self):
        return self.repository.get_all()

    # Retorna uma role pelo ID
    def get_role_by_id(self, role_id: int):
        return self.repository.get_by_id(role_id)

    # Cria uma nova role
    def create_role(self, role: RoleCreate):
        return self.repository.create(role)

    # Remove uma role pelo ID
    def delete_role(self, role_id: int):
        return self.repository.delete(role_id)
