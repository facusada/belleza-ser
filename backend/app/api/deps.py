"""Dependencias compartidas de la API."""

import secrets
from collections.abc import AsyncGenerator

from fastapi import Header, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import settings
from app.core.database import get_db as _get_db


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """Re-exporta la dependencia de sesión para poder overridearla en tests."""
    async for session in _get_db():
        yield session


async def require_admin(x_admin_key: str | None = Header(default=None)) -> None:
    """Protege endpoints de administración con la cabecera `X-Admin-Key`.

    Si `ADMIN_API_KEY` no está configurada, el endpoint queda deshabilitado (503)
    en vez de quedar abierto. La comparación es de tiempo constante.
    """
    if not settings.admin_api_key:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Admin deshabilitado: falta configurar ADMIN_API_KEY.",
        )
    if not x_admin_key or not secrets.compare_digest(x_admin_key, settings.admin_api_key):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Clave de administración inválida o ausente.",
        )
