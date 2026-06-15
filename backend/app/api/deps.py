"""Dependencias compartidas de la API."""

from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db as _get_db


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """Re-exporta la dependencia de sesión para poder overridearla en tests."""
    async for session in _get_db():
        yield session
