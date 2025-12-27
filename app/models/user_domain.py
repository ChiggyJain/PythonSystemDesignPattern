
from pydantic import BaseModel, EmailStr
from uuid import UUID


# defined our own model and inherit from Base model as pydantic concept for Business / API
class User(BaseModel):
    id: UUID
    email: EmailStr
    is_active: bool
