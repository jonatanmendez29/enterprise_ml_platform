from pydantic import BaseModel

class ForecastRequest(BaseModel):
    customer_id: str
    product_id: str
    lookback_days: int

class InventoryForecastService:
    """Service stub for inventory forecasting. Connect to BentoML in production."""

    def predict(self, parsed: dict) -> dict:
        req = ForecastRequest(**parsed)
        # TODO: integrate with BentoML and Feast for real inference
        return {"prediction": 0.0, "status": "stub", "request": req.dict()}
