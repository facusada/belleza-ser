"""Tests del endpoint de captura de leads."""

import pytest
from sqlalchemy import select

from app.core.config import settings
from app.models.lead import Lead

ADMIN_KEY = "test-admin-key"


@pytest.fixture
def admin_key(monkeypatch):
    """Configura una ADMIN_API_KEY para los tests del listado protegido."""
    monkeypatch.setattr(settings, "admin_api_key", ADMIN_KEY)
    return ADMIN_KEY


async def test_create_lead_ok(client, db_session):
    payload = {
        "name": "María Pérez",
        "email": "maria@example.com",
        "phone": "+54 9 11 1234 5678",
        "message": "Me interesa una sesión de reenergización.",
        "service_slug": "reenergizacion",
    }
    res = await client.post("/api/leads", json=payload)

    assert res.status_code == 201
    body = res.json()
    assert body["id"] > 0
    assert body["name"] == "María Pérez"
    assert body["service_slug"] == "reenergizacion"
    assert body["source"] == "contact_form"

    # Se persistió en la DB.
    rows = (await db_session.execute(select(Lead))).scalars().all()
    assert len(rows) == 1
    assert rows[0].email == "maria@example.com"


async def test_create_lead_minimal_ok(client):
    # Sólo el nombre es obligatorio.
    res = await client.post("/api/leads", json={"name": "Ana"})
    assert res.status_code == 201
    assert res.json()["email"] is None


async def test_create_lead_requires_name(client):
    res = await client.post("/api/leads", json={"message": "hola"})
    assert res.status_code == 422


async def test_create_lead_name_too_short(client):
    res = await client.post("/api/leads", json={"name": "A"})
    assert res.status_code == 422


async def test_create_lead_invalid_email(client):
    res = await client.post("/api/leads", json={"name": "Ana", "email": "no-es-email"})
    assert res.status_code == 422


async def test_list_leads_requires_key(client, admin_key):
    # Sin cabecera o con clave incorrecta -> 401.
    assert (await client.get("/api/leads")).status_code == 401
    res = await client.get("/api/leads", headers={"X-Admin-Key": "mal"})
    assert res.status_code == 401


async def test_list_leads_disabled_without_config(client, monkeypatch):
    # Si no hay ADMIN_API_KEY configurada, el endpoint queda deshabilitado (503).
    monkeypatch.setattr(settings, "admin_api_key", "")
    res = await client.get("/api/leads", headers={"X-Admin-Key": "lo-que-sea"})
    assert res.status_code == 503


async def test_list_leads_ok_ordered(client, admin_key):
    await client.post("/api/leads", json={"name": "Primero"})
    await client.post("/api/leads", json={"name": "Segundo"})

    res = await client.get("/api/leads", headers={"X-Admin-Key": admin_key})
    assert res.status_code == 200
    body = res.json()
    assert len(body) == 2
    # Más recientes primero.
    assert body[0]["name"] == "Segundo"
    assert body[1]["name"] == "Primero"
