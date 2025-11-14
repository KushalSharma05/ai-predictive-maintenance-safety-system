from ultralytics import YOLO
import cv2

model = YOLO("yolov8n.pt")  # pre-trained model

def detect_safety(image_path):
    results = model(image_path)

    helmet = False
    jacket = False

    for r in results[0].boxes:
        cls = int(r.cls[0])
        if cls == 1:  # example class (modify based on your labels)
            helmet = True
        if cls == 2:
            jacket = True

    return {
        "helmet": helmet,
        "jacket": jacket,
        "safe": helmet and jacket
    }
