# Enterprise MLOps Platform

A production-grade, scalable Machine Learning Operations platform supporting:
- Product A: Inventory planning and management (demand forecasting, stock optimisation)
- Product B: Personalised product recommendations

## Tech stack
- Feature Store: Feast + MinIO + Redis
- Tracking: MLflow
- Pipeline orchestration: Kubeflow Pipelines
- Serving: BentoML + Kubernetes + Helm
- CI/CD: GitHub Actions + Argo CD
- Monitoring: Prometheus + Grafana + Evidently

## Structure
- `src/` - model code and serving components
- `deploy/` - helm charts, kubernetes manifests
- `.github/workflows/` - CI pipeline definitions
- `infra/` - infrastructure scaffolding and docs
- `tests/` - unit/integration tests

## Getting started
1. Install dependencies (Python 3.10+, BentoML, Feast, MLflow, pytest, ruff)
2. Run linter: `ruff check src tests`
3. Run unit tests: `pytest tests`
4. (`future`) install on-local k8s via Kind and use `deploy/` charts
