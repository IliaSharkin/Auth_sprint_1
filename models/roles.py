import uuid

from sqlalchemy import VARCHAR, Column, ForeignKey, Text
from sqlalchemy.dialects.postgresql import UUID

from models.base import TimestapmMixin

from database import Base


class Role(Base, TimestapmMixin):
    __tablename__ = 'roles'

    id = Column(UUID(as_uuid=True), nullable=False, unique=True, primary_key=True, default=uuid.uuid4)
    code = Column(VARCHAR(255), nullable=False, unique=True)
    description = Column(Text, default='')
    
    def __repr__(self):
        return f'({self.code}) {self.description}'


# class UserRole(Base, TimestapmMixin):
#     __tablename__ = 'users_roles'

#     id = Column(UUID(as_uuid=True), nullable=False, unique=True, primary_key=True, default=uuid.uuid4)
#     user_id = Column(UUID(as_uuid=True), ForeignKey('users.id', ondelete='CASCADE'), nullable=False, default=uuid.uuid4)  # noqa
#     role_id = Column(UUID(as_uuid=True), ForeignKey('roles.id', ondelete='CASCADE'), nullable=False, default=uuid.uuid4)  # noqa