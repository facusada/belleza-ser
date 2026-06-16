"""Endpoint de captura de leads (formulario de contacto de la v1)."""

from fastapi import APIRouter, Depends, Query, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.deps import get_db, require_admin
from app.models.lead import Lead
from app.schemas.lead import LeadCreate, LeadRead

router = APIRouter(prefix="/api/leads", tags=["leads"])


@router.post("", response_model=LeadRead, status_code=status.HTTP_201_CREATED)
async def create_lead(payload: LeadCreate, db: AsyncSession = Depends(get_db)) -> Lead:
    """Guarda un lead del formulario de contacto en Postgres."""
    lead = Lead(
        name=payload.name,
        email=payload.email,
        phone=payload.phone,
        message=payload.message,
        service_slug=payload.service_slug,
        source="contact_form",
    )
    db.add(lead)
    await db.commit()
    await db.refresh(lead)
    return lead


@router.get("", response_model=list[LeadRead], dependencies=[Depends(require_admin)])
async def list_leads(
    db: AsyncSession = Depends(get_db),
    limit: int = Query(default=100, ge=1, le=500),
    offset: int = Query(default=0, ge=0),
) -> list[Lead]:
    """Lista los leads (más recientes primero). Requiere cabecera `X-Admin-Key`."""
    result = await db.scalars(
        select(Lead)
        .order_by(Lead.created_at.desc(), Lead.id.desc())
        .limit(limit)
        .offset(offset)
    )
    return list(result.all())
