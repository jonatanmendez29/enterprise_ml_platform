import os
import mlflow
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
RAW_DATA_PATH = os.path.join(BASE_DIR, "data", "product_a", "raw", "synthetic_inventory_data.csv")
MODEL_DIR = os.path.join(BASE_DIR, "models", "product_a")

os.makedirs(MODEL_DIR, exist_ok=True)

if __name__ == "__main__":
    df = pd.read_csv(RAW_DATA_PATH, parse_dates=["timestamp"])
    df = df.sort_values("timestamp")
    df["hour"] = df["timestamp"].dt.hour
    df["day_of_week"] = df["timestamp"].dt.dayofweek

    features = ["hour", "day_of_week", "inventory_level", "price"]
    target = "units_sold"

    X = df[features]
    y = df[target]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    with mlflow.start_run(run_name="product_a_inventory_forecast"):
        model = RandomForestRegressor(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)

        y_pred = model.predict(X_test)
        rmse = mean_squared_error(y_test, y_pred, squared=False)

        mlflow.log_param("n_estimators", 100)
        mlflow.log_metric("rmse", float(rmse))

        artifact_path = os.path.join(MODEL_DIR, "rf_inventory_forecast.pkl")
        mlflow.sklearn.log_model(model, artifact_path)

        print(f"Finished training; RMSE = {rmse:.3f}")
        print(f"Model artifact saved to {artifact_path}")
