"""Engine y sesión async de SQLAlchemy 2.0, más la Base declarativa."""

import os
from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.pool import NullPool

from app.core.config import settings


class Base(DeclarativeBase):
    """Base declarativa común a todos los modelos."""


# Serverless (Vercel) necesita NullPool: no hay proceso persistente que mantenga el pool.
_pool_kwargs = {"poolclass": NullPool} if os.getenv("VERCEL") else {}
engine = create_async_engine(settings.database_url, echo=False, future=True, **_pool_kwargs)

AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autoflush=False,
)


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """Dependencia de FastAPI: entrega una sesión y la cierra al terminar."""
    async with AsyncSessionLocal() as session:
        yield session
