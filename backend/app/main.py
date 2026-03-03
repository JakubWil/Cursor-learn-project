from fastapi import FastAPI

from app.core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
)


@app.get("/health", tags=["health"])
def health_check() -> dict[str, str]:
    """Simple health check endpoint."""
    return {"status": "ok"}


__all__ = ["app"]
