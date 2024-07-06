from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import UUID
from sqlalchemy.dialects.postgresql import UUID as PG_UUID

class Model(DeclarativeBase):
    id: Mapped[UUID] = mapped_column(PG_UUID(as_uuid=True), primary_key=True, index=True, unique=True, nullable=False, server_default=PG_UUID(as_uuid=True), default=uuid4, nullable=False)

