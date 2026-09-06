# payment-service



## Overview

| Field | Value |
|-------|-------|
| **Service** | `payment-service` |
| **Environment** | `production` |
| **Owner** | `` |
| **Port** | `` |

## Getting Started

### Local Development

```bash
# Install dependencies
pip install -r requirements.txt

# Run locally
uvicorn main:app --reload --port 
```

### Docker

```bash
# Build
docker build -t payment-service .

# Run
docker run -p : payment-service
```

## Kubernetes Deployment

The service is deployed via ArgoCD GitOps. Manifests are in `kubernetes/`.

```bash
# Check deployment status
kubectl get deployment -n payment-service

# View logs
kubectl logs -n payment-service -l app.kubernetes.io/name=payment-service -f

# Port forward for local access
kubectl port-forward -n payment-service svc/payment-service :80
```

## Monitoring

- **Grafana Dashboard**: https://grafana.platformcatalyst.dev/d/payment-service-dashboard
- **Logs**: https://grafana.platformcatalyst.dev/explore (Loki)

## API Documentation

- **OpenAPI Spec**: `spec/openapi.yaml`
- **Swagger UI**: https://payment-service.platformcatalyst.dev/docs
