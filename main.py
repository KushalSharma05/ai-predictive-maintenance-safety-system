from fastapi import FastAPI, UploadFile
from ml.predict import predict_failure
from safety.safety_detection import detect_safety
import shutil

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Predictive Maintenance & Safety API Running!"}

@app.post("/predict-maintenance")
def predict(temp: float, vibration: float, pressure: float):
    result = predict_failure(temp, vibration, pressure)
    return {"predicted_time_to_failure": result}

@app.post("/safety-check")
async def safety_check(file: UploadFile):
    with open("temp.jpg", "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    result = detect_safety("temp.jpg")
    return result
