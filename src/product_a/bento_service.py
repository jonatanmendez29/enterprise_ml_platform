from datetime import datetime
from typing import Dict

from bentoml import api, service

from .model import load_local_model, predict as forecast_predict
from .service import ForecastRequest

_service_model = None


def get_model():
    global _service_model
    if _service_model is None:
        try:
            _service_model = load_local_model()
        except FileNotFoundError:
            _service_model = None
    return _service_model


@service(name="product_a_inventory_forecast")
class InventoryForecastService:
    @api(input_spec=dict, output_spec=dict)
    def forecast(self, request: Dict) -> Dict:
        req = ForecastRequest(**request)
        event_timestamp = request.get("event_timestamp")

        if event_timestamp is None:
            event_timestamp = datetime.utcnow().isoformat()

        feature_request = {
            "customer_id": req.customer_id,
            "product_id": req.product_id,
            "event_timestamp": event_timestamp,
            "hour": request.get("hour", datetime.utcnow().hour),
            "day_of_week": request.get("day_of_week", datetime.utcnow().weekday()),
            "inventory_level": request.get("inventory_level", 0),
            "price": request.get("price", 0.0),
        }

        model = get_model()
        if model is None:
            return {
                "customer_id": req.customer_id,
                "product_id": req.product_id,
                "prediction": None,
                "status": "model_not_available",
                "timestamp": datetime.utcnow().isoformat(),
            }

        try:
            prediction_value = forecast_predict(feature_request, model)
            status = "success"
        except Exception:
            prediction_value = None
            status = "error"

        return {
            "customer_id": req.customer_id,
            "product_id": req.product_id,
            "prediction": prediction_value,
            "status": status,
            "timestamp": datetime.utcnow().isoformat(),
        }
