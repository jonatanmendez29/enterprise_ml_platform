import os
from typing import Dict, List
import joblib
from feast import FeatureStore
from sklearn.ensemble import RandomForestRegressor

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
LOCAL_MODEL_PATH = os.path.join(BASE_DIR, "models", "product_a", "rf_inventory_forecast.joblib")
FEATURE_STORE_PATH = os.path.join(BASE_DIR, "feature_repo", "product_a")
FEATURE_REFS = [
    "inventory_forecast_features:inventory_level",
    "inventory_forecast_features:price",
    "inventory_forecast_features:hour",
    "inventory_forecast_features:day_of_week",
]


def load_local_model() -> RandomForestRegressor:
    if not os.path.exists(LOCAL_MODEL_PATH):
        raise FileNotFoundError(
            f"Local model bundle not found at {LOCAL_MODEL_PATH}. Run pipelines/product_a/train.py first."
        )

    return joblib.load(LOCAL_MODEL_PATH)


def fetch_online_features(request: Dict) -> List[float]:
    fs = FeatureStore(repo_path=FEATURE_STORE_PATH)

    feature_rows = [
        {
            "customer_id": request["customer_id"],
            "product_id": request["product_id"],
            "event_timestamp": request.get("event_timestamp"),
        }
    ]

    vector = fs.get_online_features(feature_refs=FEATURE_REFS, entity_rows=feature_rows).to_dict()

    # Assert ordering
    return [
        float(vector[ref.split(":")[1]][0])
        for ref in FEATURE_REFS
    ]


def predict(request: Dict, model: RandomForestRegressor) -> float:
    features = fetch_online_features(request)
    prediction = model.predict([features])
    return float(prediction[0])
