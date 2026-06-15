"""Servicio ofrecido.

En la v1 el sitio lee los servicios desde `frontend/data/services.ts` (fuente
editable única). Esta tabla existe como terreno para la v2: cuando haya checkout,
las `Order`/`OrderItem` referenciarán servicios persistidos acá.
"""

from sqlalchemy import Boolean, Numeric, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


class Service(Base):
    __tablename__ = "services"

    id: Mapped[int] = mapped_column(primary_key=True)
    slug: Mapped[str] = mapped_column(String(80), unique=True, index=True)
    name: Mapped[str] = mapped_column(String(160))
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    # Precio opcional: en v1 puede ser NULL (no se cobra online).
    price: Mapped[float | None] = mapped_column(Numeric(12, 2), nullable=True)
    currency: Mapped[str] = mapped_column(String(3), default="ARS")
    active: Mapped[bool] = mapped_column(Boolean, default=True)
