# Belleza Ser

Landing page de **Belleza Ser** — bienestar holístico y sanación a distancia.
La v1 es **informativa** (no cobra online): los servicios se reservan por **WhatsApp** y hay
un **formulario de contacto** que guarda leads en Postgres. La arquitectura queda preparada
para sumar **e-commerce / pagos (Mercado Pago)** en una v2 sin reescribir la UI.

## Stack

| Capa      | Tecnología                                              |
|-----------|---------------------------------------------------------|
| Frontend  | Nuxt 4 · Vue 3 · TypeScript · Tailwind CSS (pnpm)       |
| Backend   | FastAPI · SQLAlchemy 2.0 async · Alembic (Python 3.11+) |
| Base de datos | PostgreSQL                                          |
| Orquestación | Docker Compose                                       |

```
belleza-ser/
├── docker-compose.yml      # db + api + web
├── .env.example            # todas las variables
├── frontend/               # Nuxt (landing one-page)
└── backend/                # FastAPI (leads + groundwork e-commerce)
```

## Levantar el proyecto

### Opción A — Docker (todo junto)

```bash
cp .env.example .env        # ajustá los valores (sobre todo el número de WhatsApp)
docker compose up --build
```

- Web:  http://localhost:3000
- API:  http://localhost:8000  (docs interactivas en http://localhost:8000/docs)
- DB:   Postgres en localhost:5432

El servicio `api` corre `alembic upgrade head` automáticamente al arrancar.

### Opción B — Nativo (desarrollo, hot-reload)

**Base de datos** (sólo Postgres por Docker):
```bash
docker compose up -d db
```

**Backend:**
```bash
cd backend
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
# Usá localhost en vez de 'db' al correr fuera de Docker:
export DATABASE_URL="postgresql+asyncpg://belleza:belleza_dev_password@localhost:5432/belleza_ser"
alembic upgrade head
uvicorn app.main:app --reload --port 8000
```

**Frontend:**
```bash
cd frontend
corepack pnpm install
corepack pnpm dev          # http://localhost:3000
```

## Dónde editar el contenido

| Qué                                   | Dónde                                                     |
|---------------------------------------|-----------------------------------------------------------|
| **Servicios** (título, descripción, precio, mensaje de WhatsApp) | [`frontend/data/services.ts`](frontend/data/services.ts) |
| **Textos** (hero, "Sobre mí", e-book, contacto, SEO)             | [`frontend/data/site.ts`](frontend/data/site.ts)         |
| **Número de WhatsApp**                | variable `NUXT_PUBLIC_WHATSAPP_NUMBER` en `.env`          |
| **Usuario de Instagram**              | variable `NUXT_PUBLIC_INSTAGRAM_USER` en `.env`           |
| **Colores / tipografías**             | [`frontend/tailwind.config.ts`](frontend/tailwind.config.ts) |
| **Imagen para compartir (OG)**        | reemplazá `frontend/public/og-image.svg` y `site.seo.ogImage` |

> El número de WhatsApp va en formato internacional, **sin** `+` ni espacios (ej. AR: `5491122334455`).

### Nota sobre la imagen de Open Graph
`og-image.svg` es un **placeholder**. WhatsApp/Instagram previsualizan mejor imágenes **PNG/JPG**
de **1200×630**. Para producción, exportá una imagen real a `frontend/public/og-image.png` y
actualizá `site.seo.ogImage` en [`frontend/data/site.ts`](frontend/data/site.ts).

## Tests

```bash
# Backend
cd backend && source .venv/bin/activate && pytest

# Frontend (builder de WhatsApp)
cd frontend && corepack pnpm test
```

## Variables de entorno

Ver [`.env.example`](.env.example). Resumen:

- **Web:** `NUXT_PUBLIC_SITE_URL`, `NUXT_PUBLIC_API_BASE`, `NUXT_PUBLIC_WHATSAPP_NUMBER`, `NUXT_PUBLIC_INSTAGRAM_USER`
- **API:** `DATABASE_URL`, `CORS_ORIGINS`, `PAYMENT_PROVIDER`
- **DB:** `POSTGRES_USER`, `POSTGRES_PASSWORD`, `POSTGRES_DB`, `POSTGRES_PORT`

## Roadmap v2 — activar pagos online

La base ya está preparada para enchufar Mercado Pago **sin reescribir** la UI ni el resto del backend:

1. **Modelo de dominio:** las tablas `services`, `orders`, `order_items` y `payments` ya existen
   (migración inicial). El sitio v1 lee los servicios de `frontend/data/services.ts`; en v2 pasarán
   a leerse desde la tabla `services`.
2. **Proveedor de pagos:** implementar `MercadoPagoProvider(PaymentProvider)` en
   `backend/app/services/payments/` cumpliendo el contrato de
   [`base.py`](backend/app/services/payments/base.py) (`create_checkout`, `handle_webhook`) y
   registrarlo en la factory ([`__init__.py`](backend/app/services/payments/__init__.py)).
3. **Configuración:** setear `PAYMENT_PROVIDER=mercadopago` y completar `MERCADOPAGO_ACCESS_TOKEN`
   y `MERCADOPAGO_WEBHOOK_SECRET` en `.env`.
4. **Endpoints nuevos:** crear las rutas de checkout (`POST /api/orders` → `create_checkout`) y el
   **webhook** de confirmación (`POST /api/payments/webhook` → `handle_webhook`) para actualizar el
   estado de la orden cuando Mercado Pago notifica el pago.
5. **Frontend:** en [`useServiceAction.ts`](frontend/composables/useServiceAction.ts), devolver una
   acción `{ kind: 'checkout', to: '/checkout/<slug>' }` para los servicios que se cobren online.
   Los componentes (`ServiceCard`, `CtaButton`) **no cambian**: ya consumen ese descriptor.

## Fuera de alcance de la v1

Pagos online reales, checkout, panel de administración de leads/órdenes y descarga del e-book
con paywall. Todo queda habilitado por el modelo de dominio y los *seams* descritos arriba.
