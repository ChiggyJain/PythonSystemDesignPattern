
from pydantic import BaseModel, EmailStr
from uuid import UUID, uuid4
from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from app.core.database import Base


# defined our own model and inherit from Base model as pydantic concept
"""
class User(BaseModel):

    # Generates globally unique ID
    # Safe for distributed systems
    # No DB dependency
    id: UUID
    email: EmailStr
    is_active: bool = True

    # Factory pattern starter
    # Controls object creation
    # Enforces rules at one place
    @classmethod
    def create(cls, email: EmailStr):
        return cls(
            id=uuid4(),
            email=email,
            is_active=True
        )

"""

# defined our own UserDB class model act as DB-Table and inherit from Base class
# SQLAlchemy 2.x STYLE: Explicit typing, Better async support
class UserDB(Base):

    # table-name
    __tablename__ = "users"
    # columns
    id: Mapped[str] = mapped_column(
        String(36), primary_key=True, default=lambda: str(uuid4())
    )
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)