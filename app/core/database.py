
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    AsyncSession,
)
from sqlalchemy.orm import declarative_base


# database url
DATABASE_URL = (
    "mysql+asyncmy://c:Dharmilal%407186@localhost:3306/system_design_db"
)

# database async engine
# Async DB connection pool
# Non-blocking I/O
engine = create_async_engine(
    DATABASE_URL,
    # print all sql statement on terminal
    echo=True,
    # Max persistent connections
    pool_size=10,
    # Temporary burst handling
    max_overflow=20,
)

# database session
# Factory that creates DB sessions
# One session per request
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    # Keeps objects alive after commit
    expire_on_commit=False
)

# Base class for all DB tables
# Keeps DB schema centralized
Base = declarative_base()

