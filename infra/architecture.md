# Architecture Overview

This repository implements the Enterprise MLOps Platform architecture described in `info.md`.

## Logical Layers

1. Data Ingestion & Feature Store (Feast + MinIO + Redis).
2. Model Development & Experimentation (MLflow + notebooks).
3. Training Pipeline Orchestration (Kubeflow Pipelines + Great Expectations).
4. Model Serving (BentoML + Kubernetes + Helm blue/green).
5. CI/CD & GitOps (GitHub Actions + Argo CD).
6. Monitoring/Observability (Prometheus + Grafana + Evidently).
7. Security & Compliance (RBAC, secrets, TLS, GDPR/CCPA).

## Component skeleton

- `src/product_a/` and `src/product_b/`: BentoML service stubs + model entry points.
- `deploy/helm/`: Helm charts for both product services.
- `.github/workflows/ci.yml`: lint & test pipeline.
- `tests/`: initial pytest tests (TDD skeleton).

## Next milestones

1. Setup Feast repo and feature set definitions (Product A first). 
2. Implement training pipeline for Product A (data generation -> training -> MLflow model logging).
3. Add Psi/bento model serve path with Kubernetes Helm chart from deploy/helm/product-a.
4. Add BDD coverage (pytest-bdd) for Product A key scenario.
5. Implement model inference route and Prometheus metrics exporter.
