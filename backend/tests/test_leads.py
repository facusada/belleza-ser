"""Tests del endpoint de captura de leads."""

from sqlalchemy import select

from app.models.lead import Lead


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
