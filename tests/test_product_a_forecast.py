from pytest_bdd import scenario, given, when, then

from src.product_a.service import InventoryForecastService

forecast_request_data = {}
forecast_response_data = {}

@scenario('features/product_a_forecast.feature', 'Request forecast for a product and get valid response')
def test_product_a_forecast():
    pass


@given('a forecast request event')
def set_forecast_request_event():
    global forecast_request_data
    forecast_request_data = {
        'customer_id': 'C123',
        'product_id': 'P770',
        'lookback_days': 14,
        'hour': 9,
        'day_of_week': 2,
        'inventory_level': 40,
        'price': 50.0,
    }


@when('the forecast service processes the request')
def process_forecast_request():
    global forecast_response_data
    service = InventoryForecastService()
    forecast_response_data = service.predict(forecast_request_data)


@then('the response includes a prediction key')
def check_prediction_key():
    assert 'prediction' in forecast_response_data
