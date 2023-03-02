import datetime

from sqlalchemy import TIMESTAMP, Column



class TimestapmMixin(object):
    created_at = Column(TIMESTAMP, nullable=False, default=datetime.datetime.now())
    updated_at = Column(TIMESTAMP, nullable=False, default=datetime.datetime.now(), onupdate=datetime.datetime.now())

class IDMixin:
    pass