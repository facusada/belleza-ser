"""Punto de entrada de la API de Belleza Ser."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import health, leads
from app.core.config import settings

app = FastAPI(
    title="Belleza Ser API",
    version="0.1.0",
    description="Captura de leads para la landing. Groundwork para e-commerce (v2).",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router)
app.include_router(leads.router)


@app.get("/", tags=["health"])
async def root() -> dict[str, str]:
    return {"service": "belleza-ser-api", "docs": "/docs"}
