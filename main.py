import logging
import os

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

_APP_NAME = os.getenv("APP_NAME", "payment-service")
_APP_ENV = os.getenv("APP_ENV", "development")
_LOG_LEVEL = os.getenv("LOG_LEVEL", "info")
_PORT = int(os.getenv("PORT", "8000"))

logging.basicConfig(
    level=getattr(logging, _LOG_LEVEL.upper(), logging.INFO),
    format="%(asctime)s %(levelname)s %(name)s %(message)s",
)
logger = logging.getLogger(_APP_NAME)

app = FastAPI(
    title=_APP_NAME,
    version="1.0.0",
    description="Simple FastAPI microservice used to test the Project Catalyst scaffolder deploy template.",
)

_ITEMS = [
    {"id": 1, "name": "alpha", "description": "First sample item"},
    {"id": 2, "name": "beta", "description": "Second sample item"},
    {"id": 3, "name": "gamma", "description": "Third sample item"},
]


class Item(BaseModel):
    name: str
    description: str = ""


@app.get("/health")
def health() -> dict:
    """Liveness/readiness probe endpoint used by the Kubernetes deployment."""
    return {"status": "ok"}


@app.get("/")
def root() -> dict:
    """Service metadata."""
    return {
        "service": _APP_NAME,
        "environment": _APP_ENV,
        "version": "1.0.0",
        "docs": "/docs",
        "health": "/health",
    }


@app.get("/version")
def version() -> dict:
    """Simple version endpoint."""
    return {"service": _APP_NAME, "version": "1.0.0"}


@app.get("/api/v1/items")
def list_items() -> list[dict]:
    """List all sample items."""
    return _ITEMS


@app.get("/api/v1/items/{item_id}")
def get_item(item_id: int) -> dict:
    """Fetch a single sample item by id."""
    item = next((i for i in _ITEMS if i["id"] == item_id), None)
    if item is None:
        raise HTTPException(status_code=404, detail=f"Item {item_id} not found")
    return item


@app.post("/api/v1/items")
def create_item(item: Item) -> dict:
    """Add a new sample item (in-memory; resets on restart)."""
    new_id = max((i["id"] for i in _ITEMS), default=0) + 1
    entry = {"id": new_id, "name": item.name, "description": item.description}
    _ITEMS.append(entry)
    logger.info("created item id=%s name=%s", new_id, item.name)
    return entry