import joblib
import numpy as np

model = joblib.load("maintenance_model.pkl")

def predict_failure(temp, vib, pres):
    input_data = np.array([[temp, vib, pres]])
    prediction = model.predict(input_data)[0]
    return prediction
