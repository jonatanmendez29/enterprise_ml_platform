#!/usr/bin/env bash
set -euo pipefail

export MINIO_ENDPOINT=http://localhost:9000
export MINIO_ACCESS_KEY=minioadmin
export MINIO_SECRET_KEY=minioadmin

export REDIS_HOST=localhost
export REDIS_PORT=6379

export FEAST_REPO_PATH="$(pwd)/feature_repo/product_a"
export MLFLOW_TRACKING_URI=http://localhost:5000
