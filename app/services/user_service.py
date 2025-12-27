
from pydantic import EmailStr
from uuid import uuid4
from app.models.user_domain import User
from app.repositories.user_repository import UserRepository



# defined our own service class
class UserService:

    # own constructor
    def __init__(self, repository: UserRepository):
        self.repository = repository

    # defined our own async function
    async def register_user(self, email: EmailStr) -> User:
        # Business Rule and validation
        if not email.endswith("@company.com"):
            raise ValueError("Only company emails allowed")
        existing = await self.repository.get_by_email(email)
        if existing:
            raise ValueError("User already exists")
        # creating user object and Entity initialized
        user = User(
            id=uuid4(),
            email=email,
            is_active=True,
        )
        # respository responsibility [Talks to DB, Talks to cache, Talks to external systems]
        return await self.repository.save(user)
