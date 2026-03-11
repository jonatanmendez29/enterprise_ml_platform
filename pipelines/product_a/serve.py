import os
import joblib
import pandas as pd
from src.product_a.service import InventoryForecastService

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODEL_PATH = os.path.join(BASE_DIR, "models", "product_a", "rf_inventory_forecast.pkl")


def load_model():
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(f"Model not found at {MODEL_PATH}. Run train script first.")
    return joblib.load(MODEL_PATH)


def predict_from_sample(model, sample):
    request = {
        "customer_id": sample["customer_id"],
        "product_id": sample["product_id"],
        "lookback_days": 7,
        "hour": sample["hour"],
        "day_of_week": sample["day_of_week"],
        "inventory_level": sample["inventory_level"],
        "price": sample["price"],
    }
    result = model.predict([[sample["hour"], sample["day_of_week"], sample["inventory_level"], sample["price"]]])
    service = InventoryForecastService()
    return service.predict(request), float(result[0])
