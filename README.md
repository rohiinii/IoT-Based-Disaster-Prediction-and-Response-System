# IoT-Based-Disaster-Prediction-and-Response-System

A smart, end-to-end disaster monitoring system that integrates **IoT sensors**, **cloud platforms**, and **machine learning** to predict **wildfires** and **heatwaves**. It simulates real-time environmental data using Wokwi, transmits via MQTT to ThingSpeak, and uses XGBoost models for prediction. Alerts are sent instantly via email when risks are detected.

---

## 🚀 Project Overview

- **Goal**: Build a modular, scalable system to monitor temperature, humidity, wind speed, and air quality for disaster prediction.
- **Approach**: Combine simulated sensor data with historical training datasets using machine learning.
- **Outcome**: Real-time alert generation for extreme weather events like heatwaves and wildfires.

---

## 🔧 Technologies Used

| Layer        | Tools/Platforms                                  |
|--------------|--------------------------------------------------|
| IoT Hardware | ESP32, DHT22, MQ-135, Potentiometer, LDR (Wokwi) |
| Data Cloud   | MQTT, ThingSpeak                                  |
| ML Training  | Python, XGBoost, Random Forest             |
| Alerts       | Python `smtplib`, Gmail SMTP                      |

---

## 📡 How It Works

1. **Simulate Environment**: Sensors simulate live conditions using Wokwi (ESP32 + sensors).
2. **Publish to Cloud**: Data is sent to ThingSpeak over MQTT.
3. **Fetch + Predict**: A Python script pulls the data and runs predictions using trained ML models.
4. **Send Alerts**: If conditions match trained risk profiles, email alerts are automatically sent.

---

## 📊 Machine Learning Models

| Model               | Dataset Source                        | Accuracy |
|---------------------|----------------------------------------|----------|
| Heatwave Predictor  | NOAA U.S. Temp Anomaly Dataset         | 100%     |
| Wildfire Predictor  | Kaggle California Fire Weather Dataset | 95%+     |

- Trained using **XGBoost** with `joblib` for deployment.
- Features: `temperature`, `wind speed`, `air quality`.

---

## ✅ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/iot-disaster-prediction.git
cd iot-disaster-prediction
```

Install dependencies
```bash
pip install pandas scikit-learn xgboost joblib requests
```

Configure your credentials in alert.py
```bash
Add your Gmail app password and recipient email
```

Run the script
```bash 
IoT_Final_Project.py
```

---

## 📦 Data Sources
🌡️ NOAA Temperature Anomaly Dataset

🔥 California Wildfire Dataset – Kaggle
