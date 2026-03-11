from src.product_a import model


class DummyFeatureVector:
    def __init__(self, data):
        self._data = data

    def to_dict(self):
        return self._data


class DummyFeatureStore:
    def __init__(self, repo_path):
        self.repo_path = repo_path

    def get_online_features(self, feature_refs, entity_rows):
        # return consistent feature vector for test
        return DummyFeatureVector({
            "inventory_level": [50],
            "price": [25.0],
            "hour": [10],
            "day_of_week": [3],
        })


def test_fetch_online_features(monkeypatch):
    monkeypatch.setattr(model, "FeatureStore", DummyFeatureStore)
    request = {
        "customer_id": "C101",
        "product_id": "P770",
        "event_timestamp": "2025-01-31T12:00:00",
    }

    features = model.fetch_online_features(request)
    assert features == [50.0, 25.0, 10.0, 3.0]


def test_predict_with_dummy_model(monkeypatch):
    class DummyModel:
        def predict(self, X):
            assert X == [[50.0, 25.0, 10.0, 3.0]]
            return [123.45]

    monkeypatch.setattr(model, "FeatureStore", DummyFeatureStore)
    request = {
        "customer_id": "C101",
        "product_id": "P770",
        "event_timestamp": "2025-01-31T12:00:00",
    }
    value = model.predict(request, DummyModel())
    assert value == 123.45
