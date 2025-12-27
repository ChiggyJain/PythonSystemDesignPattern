
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import BaseModel, EmailStr
from app.api.deps import get_db
from app.repositories.user_repository import UserRepository
from app.services.user_service import UserService
from app.api.deps import get_user_service


router = APIRouter()


# defined our own pydantic mode and inherit from base model
class UserCreateRequest(BaseModel):
    email: EmailStr


"""
Reads JSON body, Converts it into UserCreateRequest, Validates email format,
Rejects bad input before business logic
"""
@router.post("/users")
async def create_user(
    payload: UserCreateRequest,
    service: UserService = Depends(get_user_service),
):
    
    try:
        # calling async function of service object
        user = await service.register_user(payload.email)
        return user
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
