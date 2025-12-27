
import asyncio
from app.core.database import engine, Base
from app.models.user import UserDB

async def init():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

if __name__ == "__main__":
    asyncio.run(init())
