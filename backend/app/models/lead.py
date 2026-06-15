"""Lead / consulta entrante. Es la entidad que SÍ se usa en la v1."""

from datetime import datetime

from sqlalchemy import DateTime, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


class Lead(Base):
    __tablename__ = "leads"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120))
    email: Mapped[str | None] = mapped_column(String(255), nullable=True)
    phone: Mapped[str | None] = mapped_column(String(40), nullable=True)
    message: Mapped[str | None] = mapped_column(Text, nullable=True)
    # Slug del servicio de interés (referencia laxa a data/services.ts del front).
    service_slug: Mapped[str | None] = mapped_column(String(80), nullable=True)
    # De dónde vino el lead: "contact_form", "whatsapp", etc.
    source: Mapped[str] = mapped_column(String(40), default="contact_form")
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
