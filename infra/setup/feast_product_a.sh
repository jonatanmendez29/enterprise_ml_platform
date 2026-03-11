#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"

export MINIO_ENDPOINT=http://localhost:9000
export MINIO_ACCESS_KEY=minioadmin
export MINIO_SECRET_KEY=minioadmin

export REDIS_HOST=localhost
export REDIS_PORT=6379

echo "[INFO] Starting local infra via docker-compose..."
cd "$ROOT_DIR"

docker compose -f infra/docker-compose.yml up -d

echo "[INFO] Creating synthetic Product A data..."
python data/generate_product_a_data.py

echo "[INFO] Training Product A model..."
python pipelines/product_a/train.py

echo "[INFO] Initializing Feast feature repo for Product A..."
cd "$ROOT_DIR/feature_repo/product_a"

# Ensure feature repository path is correct for Feast
feast apply

# harvest features into online store (past 30 days option)
feast materialize 2025-01-01T00:00:00 2026-01-01T00:00:00

echo "[INFO] Feast Product A setup done."

echo "Use 'docker compose -f infra/docker-compose.yml ps' to inspect services."