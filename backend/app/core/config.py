"""Configuración de la app, leída de variables de entorno con pydantic-settings."""

from functools import lru_cache

from pydantic import field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

_DEFAULT_DB_URL = "postgresql+asyncpg://belleza:belleza_dev_password@localhost:5432/belleza_ser"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    # Conexión async a Postgres (asyncpg). En docker el host es `db`.
    database_url: str = _DEFAULT_DB_URL

    # Orígenes permitidos por CORS, coma-separados.
    cors_origins: str = "http://localhost:3000"

    # Proveedor de pagos: "stub" en v1; "mercadopago" cuando se active el cobro.
    payment_provider: str = "stub"

    # Credenciales de Mercado Pago (futuro). Vacías en v1.
    mercadopago_access_token: str = ""
    mercadopago_webhook_secret: str = ""

    # Clave para endpoints de administración (listar leads). Vacía = admin deshabilitado.
    admin_api_key: str = ""

    @field_validator("database_url", mode="before")
    @classmethod
    def _fallback_empty_db_url(cls, v: object) -> object:
        if isinstance(v, str) and not v.strip():
            return _DEFAULT_DB_URL
        return v

    @field_validator("payment_provider", mode="before")
    @classmethod
    def _fallback_empty_payment_provider(cls, v: object) -> object:
        if isinstance(v, str) and not v.strip():
            return "stub"
        return v

    @property
    def cors_origins_list(self) -> list[str]:
        return [origin.strip() for origin in self.cors_origins.split(",") if origin.strip()]


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
