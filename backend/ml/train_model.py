import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib

def train_model():
    df = pd.read_csv("../../data/machine_sensor_data.csv")

    X = df[['temperature', 'vibration', 'pressure']]
    y = df['time_to_failure']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    model = RandomForestRegressor()
    model.fit(X_train, y_train)

    joblib.dump(model, "maintenance_model.pkl")
    print("Model trained and saved successfully!")

if __name__ == "__main__":
    train_model()

