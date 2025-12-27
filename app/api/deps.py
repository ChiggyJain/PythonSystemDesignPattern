
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import AsyncSessionLocal
from fastapi import Depends
from app.repositories.user_repository import UserRepository
from app.services.user_service import UserService
from app.factories.notification_adapter_factory import NotificationAdapterFactory
from app.services.notification_service import NotificationService

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session

def get_user_repository(db: AsyncSession = Depends(get_db)) -> UserRepository:
    return UserRepository(db)

def get_user_service(repo: UserRepository = Depends(get_user_repository)) -> UserService:
    return UserService(repo)


def get_notification_service(channel: str = "email") -> NotificationService:
    adapter = NotificationAdapterFactory.get_adapter(channel)
    return NotificationService(adapter)