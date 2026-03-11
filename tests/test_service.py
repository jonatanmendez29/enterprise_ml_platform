import pytest

from src.product_a.service import ForecastRequest
from src.product_b.service import RecommendationRequest


def test_forecast_request_model():
    req = ForecastRequest(customer_id="C1", product_id="P1", lookback_days=30)
    assert req.customer_id == "C1"
    assert req.lookback_days == 30


def test_recommendation_request_model():
    req = RecommendationRequest(user_id="U1", num_items=5)
    assert req.user_id == "U1"
    assert req.num_items == 5
