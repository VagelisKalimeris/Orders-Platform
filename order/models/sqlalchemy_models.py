import uuid

from sqlalchemy import Column, Integer, String, DATE
from sqlalchemy import engine # noqa
from sqlalchemy.dialects.postgresql import UUID


from order.repositories.db_repository.postgres import Base


class Order(Base):
    __tablename__ = 'order'

    id = Column(UUID(as_uuid=True), primary_key=True, unique=True, nullable=False, default=uuid.uuid4)
    stoks = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)
