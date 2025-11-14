# AI-Powered Predictive Maintenance and Smart Safety Monitoring System

This project provides an end-to-end prototype of a factory monitoring system powered by Artificial Intelligence.  
It includes **machine failure prediction**, **smart safety monitoring using computer vision**, and **real-time alerts**.

---

## 🚀 Features

### 🔧 Predictive Maintenance
- Predicts **time-to-failure** using machine learning.
- Uses sensor data (temperature, vibration, pressure).
- Helps reduce unplanned downtime.
- Automatically triggers alerts when machines approach failure.

### 🛡 Smart Safety Monitoring
- Uses YOLO-based computer vision.
- Detects whether workers are wearing:
  - Helmet
  - Safety jacket
- Generates instant alerts for safety violations.

### ⚙ Automated Scheduler
- Runs maintenance predictions at regular intervals.
- Works similar to cron jobs.
- Notifies when a machine needs urgent maintenance.

### 🌐 FastAPI Backend
- API for maintenance prediction.
- API for safety monitoring (image upload).
- Can be integrated with dashboards or factory systems.

### 💻 Simple Frontend Dashboard
- HTML-based interface.
- Lets users input sensor values and see predictions instantly.

---

## 📂 Project Structure

ai-predictive-maintenance-safety-system/
│
├── backend/
│ ├── api/
│ │ └── main.py
│ ├── ml/
│ │ ├── train_model.py
│ │ └── predict.py
│ ├── safety/
│ │ └── safety_detection.py
│ ├── scheduler/
│ │ └── maintenance_scheduler.py
│ └── requirements.txt
│
├── data/
│ ├── machine_sensor_data.csv
│ 
│
├── frontend/
│ └── index.html
│
└── README.md
