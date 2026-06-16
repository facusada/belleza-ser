"""Seed idempotente de la tabla `services`.

La fuente de verdad de los servicios en la v1 es `frontend/data/services.ts`.
Este script replica esos slugs/nombres/descripciones en la tabla `services`
(terreno para el checkout de la v2). Es idempotente: hace upsert por `slug`,
así que se puede correr cuantas veces haga falta sin duplicar.

`leads` NO se seedea: son envíos reales del formulario de contacto.

Uso:
    python -m app.seed
"""

import asyncio

from sqlalchemy import select

from app.core.database import AsyncSessionLocal
from app.models.service import Service

# Espejo de frontend/data/services.ts (price queda NULL: no se cobra online en v1).
SERVICES: list[dict[str, object]] = [
    {
        "slug": "reenergizacion",
        "name": "Sesiones de Reenergetización",
        "description": (
            "Una técnica que alinea todos los cuerpos —mental, emocional, físico y "
            "espiritual— a través de la apertura de consciencia en cada persona. Solo "
            "la propia consciencia puede lograr cambios profundos y radicales en cada "
            "ser. La Reenergetización permite un cambio en las estructuras, patrones y "
            "mandatos que puedan estar alterando el equilibrio de los cuerpos. Esta "
            "herramienta profundiza en la sanación, limpiando todo bloqueo, registro "
            "familiar ancestral y mal karma."
        ),
    },
    {
        "slug": "biodecodificacion",
        "name": "Sesiones de biodecodificación",
        "description": (
            "Un acompañamiento para entender qué emoción o conflicto está detrás de un "
            "síntoma o situación que se repite. A través del diálogo y la "
            "decodificación, encontramos el sentido y abrimos el camino para sanarlo."
        ),
    },
    {
        "slug": "cartas-numerologicas",
        "name": "Cartas numerológicas",
        "description": (
            "En esta carta encontrarás herramientas para alinearte con tu misión de "
            "vida y entender qué te impide ser lo que realmente querés. A través de tu "
            "fecha de nacimiento y tu nombre completo, realizamos un análisis que te "
            "sirva de guía en tu vida, volviéndote un observador de vos mismo y "
            "logrando así liberar tus bloqueos. ¿Estás necesitando un cambio y no "
            "sabés por dónde empezar? La numerología te puede ayudar. Disponible en "
            "cartas personales y de pareja."
        ),
    },
    {
        "slug": "ebook",
        "name": "E-book",
        "description": (
            "Un material descargable con prácticas y reflexiones para sostener tu "
            "bienestar en lo cotidiano. Pensado para que puedas volver a él cada vez "
            "que lo necesites."
        ),
    },
]


async def seed_services() -> None:
    async with AsyncSessionLocal() as session:
        created, updated = 0, 0
        for data in SERVICES:
            existing = await session.scalar(
                select(Service).where(Service.slug == data["slug"])
            )
            if existing is None:
                session.add(Service(active=True, currency="ARS", **data))
                created += 1
            else:
                existing.name = data["name"]  # type: ignore[assignment]
                existing.description = data["description"]  # type: ignore[assignment]
                existing.active = True
                updated += 1
        await session.commit()
        print(f"services seed -> creados: {created}, actualizados: {updated}")


if __name__ == "__main__":
    asyncio.run(seed_services())
