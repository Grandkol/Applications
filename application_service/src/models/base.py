from datetime import datetime
import uuid
from uuid import UUID

from sqlalchemy import MetaData
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

meta = MetaData(schema="public")


class Base(DeclarativeBase):
    metadata = meta

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid.uuid4)


class Application(Base):
    __tablename__ = "application"
    user_name: Mapped[str] = mapped_column(nullable=True)
    description: Mapped[str] = mapped_column(nullable=True)
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)