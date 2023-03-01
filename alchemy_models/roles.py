import uuid

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, ForeignKey, VARCHAR

from database import Base
from models.base import TimestapmMixin


class Role(TimestapmMixin):
    __tablename__ = 'roles'

    code = Column(VARCHAR(255), nullable=False, unique=True)
    description = Column(Base.Text, default='')

    def __repr__(self):
        return f'({self.code}) {self.description}'


class UserRole(TimestapmMixin):
    __tablename__ = 'users_roles'

    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id', ondelete='CASCADE'), nullable=False, default=uuid.uuid4)  # noqa
    role_id = Column(UUID(as_uuid=True), ForeignKey('roles.id', ondelete='CASCADE'), nullable=False, default=uuid.uuid4)  # noqa