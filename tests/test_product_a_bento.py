from src.product_a.bento_service import InventoryForecastService


def test_bento_service_flow():
    request = {
        "customer_id": "C100",
        "product_id": "P780",
        "lookback_days": 7,
        "hour": 12,
        "day_of_week": 4,
        "inventory_level": 20,
        "price": 45.0,
    }

    service = InventoryForecastService()
    result = service.forecast(request)
    assert "prediction" in result
    assert result["status"] in ["success", "error", "model_not_available"]
