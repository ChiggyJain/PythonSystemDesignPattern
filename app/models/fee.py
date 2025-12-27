from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Float
from app.core.database import Base
from uuid import uuid4

class FeeDB(Base):
    __tablename__ = "fees"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid4()))
    student_id: Mapped[str] = mapped_column(String(36))
    amount: Mapped[float] = mapped_column(Float)
    status: Mapped[str] = mapped_column(String(20))
