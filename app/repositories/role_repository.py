from app.models.role_model import Role, RoleCreate
from app.connection.database import database  # Importe a instância do banco

class RoleRepository:
    
    def get_all(self):
        """
        Retorna todas as roles do banco de dados.
        """
        with database.get_session() as session:
            return session.query(Role).all()

    def get_by_id(self, role_id: int):
        """
        Retorna uma role pelo ID.
        """
        with database.get_session() as session:
            return session.query(Role).filter(Role.id == role_id).first()

    def create(self, role_data: RoleCreate):
        """
        Cria uma nova role.
        """
        with database.get_session() as session:
            db_role = Role(name=role_data.name, description=role_data.description)
            session.add(db_role)
            session.commit()
            session.refresh(db_role)
            return db_role

    def delete(self, role_id: int):
        """
        Deleta uma role pelo ID.
        """
        with database.get_session() as session:
            role = session.query(Role).filter(Role.id == role_id).first()
            if role:
                session.delete(role)
                session.commit()
                return True
            return False
