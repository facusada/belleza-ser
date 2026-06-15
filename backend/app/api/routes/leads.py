"""Endpoint de captura de leads (formulario de contacto de la v1)."""

from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.deps import get_db
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
