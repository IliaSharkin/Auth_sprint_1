import datetime

from sqlalchemy.dialects.postgresql import INET
from sqlalchemy.ext.hybrid import hybrid_property
from werkzeug.security import check_password_hash, generate_password_hash
from sqlalchemy import Column, ForeignKey, TEXT, VARCHAR, BOOLEAN, TIMESTAMP

from database import Base
from models.base import TimestapmMixin


class User(TimestapmMixin):
    __tablename__ = 'users'

    username = Column(VARCHAR(255), nullable=False, unique=True)
    pwd_hash = Column(VARCHAR(255))
    is_superuser = Column(BOOLEAN(), default=False)
    data_joined = Column(TIMESTAMP(), default=datetime.datetime.now())
    terminate_date = Column(TIMESTAMP())

    def __repr__(self):
        return f'{self.username}'

    @hybrid_property
    def password(self):
        return self.pwd_hash

    @password.setter
    def password(self, value):
        """Store the password as a hash for security."""
        self.pwd_hash = generate_password_hash(value)

    def check_password(self, value):
        return check_password_hash(self.pwd_hash, value)


class UserData(TimestapmMixin):
    __tablename__ = 'users_data'

    user_id = Column(ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    first_name = Column(TEXT())
    last_name = Column(TEXT())
    email = Column(TEXT())
    birth_date = Column(TIMESTAMP())
    phone = Column(TEXT())
    city = Column(TEXT())

    def __repr__(self):
        return f'{self.first_name} {self.last_name}'


class UserDevice(TimestapmMixin):
    __tablename__ = 'users_device'

    user_id = Column(ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    ip = Column(INET())
    device_key = Column(TEXT())
    user_agent = Column(TEXT())

    def __repr__(self):
        return f'{self.ip} {self.user_agent}'