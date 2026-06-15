"""Configuración de la app, leída de variables de entorno con pydantic-settings."""

from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    # Conexión async a Postgres (asyncpg). En docker el host es `db`.
    database_url: str = "postgresql+asyncpg://belleza:belleza_dev_password@localhost:5432/belleza_ser"

    # Orígenes permitidos por CORS, coma-separados.
    cors_origins: str = "http://localhost:3000"

    # Proveedor de pagos: "stub" en v1; "mercadopago" cuando se active el cobro.
    payment_provider: str = "stub"

    # Credenciales de Mercado Pago (futuro). Vacías en v1.
    mercadopago_access_token: str = ""
    mercadopago_webhook_secret: str = ""

    @property
    def cors_origins_list(self) -> list[str]:
        return [origin.strip() for origin in self.cors_origins.split(",") if origin.strip()]


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
