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
1. Install dependencies (Python 3.10+, BentoML, Feast, MLflow, pytest, ruff).
   - `pip install -r requirements.txt`
2. Generate synthetic product A data:
   - `python data/generate_product_a_data.py`
3. Train product A model:
   - `python pipelines/product_a/train.py`
4. Run BDD tests:
   - `pytest -q`
5. Build BentoML service (Product A):
   - `bentoml build` (future step after `bentoml_service.py` integration if using BentoML yaml)
6. Deploy to Kubernetes via Helm chart:
   - `helm install product-a deploy/helm/product-a --namespace dev`
