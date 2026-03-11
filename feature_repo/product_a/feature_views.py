from feast import FeatureView, Field, ValueType, Feature, FileSource
from .entity import customer, product

inventory_source = FileSource(
    path="../data/product_a/raw/synthetic_inventory_data.csv",
    event_timestamp_column="timestamp",
)

inventory_features = FeatureView(
    name="inventory_forecast_features",
    entities=[customer, product],
    ttl=None,
    schema=[
        Field(name="inventory_level", dtype=ValueType.INT32),
        Field(name="price", dtype=ValueType.FLOAT),
        Field(name="hour", dtype=ValueType.INT32),
        Field(name="day_of_week", dtype=ValueType.INT32),
    ],
    source=inventory_source,
    tags={"product": "A"},
)
