
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.user import UserDB
from app.models.user_domain import User


# defined our own respository
"""
class UserRepository:

    # defined our own async save function
    async def save(self, user: User) -> User:
        # Simulating async DB save
        await self._fake_db_latency()
        return user

    # defined our own async save function
    async def _fake_db_latency(self):
        import asyncio
        await asyncio.sleep(0.2)
"""


# defined our own respository
class UserRepository:

    # defined our own constructor and intialize db-session
    def __init__(self, session: AsyncSession):
        self.session = session

    # defined our own async save function
    async def save(self, user: User) -> User:
        db_user = UserDB(
            id=str(user.id),
            email=user.email,
            is_active=user.is_active,
        )
        self.session.add(db_user)
        await self.session.commit()
        return user


    # defined our own async function
    async def get_by_email(self, email: str) -> User | None:
        stmt = select(UserDB).where(UserDB.email == email)
        result = await self.session.execute(stmt)
        row = result.scalar_one_or_none()
        if not row:
            return None
        return User(
            id=row.id,
            email=row.email,
            is_active=row.is_active,
        )