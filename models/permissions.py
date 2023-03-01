from sqlalchemy import VARCHAR, Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
import uuid

from database import Base
from models.base import TimestapmMixin


class Permission(Base, TimestapmMixin):
    __tablename__ = 'permissions'

    id = Column(UUID(as_uuid=True), nullable=False, unique=True, primary_key=True, default=uuid.uuid4)
    code = Column(VARCHAR(255), nullable=False, unique=True)

    def __repr__(self):
        return f'({self.code}) {self.description}'


class RolePermissions(Base, TimestapmMixin):
    __tablename__ = 'roles_permissions'

    id = Column(UUID(as_uuid=True), nullable=False, unique=True, primary_key=True, default=uuid.uuid4)
    role_id = Column(ForeignKey('roles.id', ondelete='CASCADE'), nullable=False)
    perm_id = Column(ForeignKey('permissions.id', ondelete='CASCADE'), nullable=False)


def create_permissions():
    permissions = [
        'users',
        'personal_data',
        'roles',
    ]

    for permission_code in permissions:
        permission = Permission.query.filter_by(code=permission_code).first()
        if not permission:
            Base.session.add(Permission(code=permission_code))
    Base.session.commit()