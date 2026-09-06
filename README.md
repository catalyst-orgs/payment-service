# payment-service

Simple FastAPI microservice used to validate the Project Catalyst scaffolder deploy template.

## Overview

| Field | Value |
|-------|-------|
| **Service** | `payment-service` |
| **Environment** | `development` |
| **Owner** | `user:default/ezzdddinnemhamdi` |
| **Port** | `8000` |

## Getting Started

### Local Development

```bash
pip install -r requirements.txt

uvicorn main:app --reload --port 8000
```

### Docker

```bash
docker build -t payment-service .

docker run -p 8000:8000 payment-service
```

## Endpoints

- `GET /health` - Liveness/readiness probe
- `GET /` - Service metadata
- `GET /version` - Version info
- `GET /api/v1/items` - List sample items
- `GET /api/v1/items/{id}` - Fetch one item
- `POST /api/v1/items` - Create an item (in-memory)

## API Documentation

- OpenAPI spec served at `/docs` when running.