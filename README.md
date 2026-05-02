# 💳 Credit Card Fraud Detection System

A machine learning-powered API built with FastAPI and PyTorch to detect fraudulent transactions in real-time.

---

## 🚀 Features

* 🔍 Real-time fraud detection
* ⚡ FastAPI high-performance backend
* 🧠 PyTorch trained model
* 📊 Logging system (latency, throughput, CPU, memory)
* 🗂 SQLite database for monitoring

---

## 🏗 Project Structure

```
Credit Card Fraud Detection System/
│
├── scoring_process.txt
├── requirements.txt            # Project dependencies
├── README.md
├── experiment.csv
│
├── prototypemodel/
│   ├── Model/
│   │   └── model.pth           # Prototype trained model
│   │
│   └── Data/
│       ├── X_train
│       ├── y_train
│       ├── X_test
│       └── y_test
│
├── E1/                         # Experiment 1 (Improved pipeline)
│   ├── Model/
│   │   └── model.pth           # Final / improved model
│   │
│   └── Data/
│       ├── X_train
│       ├── y_train
│       ├── X_dev
│       ├── y_dev
│       ├── X_test
│       └── y_test
│
└── serving/                   # API & inference layer
    ├── app.py                 # FastAPI application
    ├── model.py               # Load model & prediction logic
    ├── build_database.py      # Initialize SQLite database
    ├── run.py                 # Run server
    ├── test.py                # API testing
    ├── model.log              # Logs
    └── logging.db             # Runtime logs database
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/mahmoudhassan112/credit-card-fraud-detection-system.git
cd credit-card-fraud-detection-system
```

---

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the API

```bash
uvicorn app:app --reload
```

Open:

```
http://127.0.0.1:8000/docs
```

---

## 📡 API Endpoint

### POST `/predict`

#### Example Request:

```json
{
  "Time": 10000,
  "V1": -1.23,
  "V2": 0.45,
  "...": "...",
  "Amount": 250.0
}
```

---

#### Example Response:

```json
{
  "label": "Fraud"
}
```

---

## 📊 Logging System

Each request logs:

* request_id
* timestamp
* prediction
* probability_output
* latency (ms)
* throughput (req/sec)
* CPU & memory usage
* status (SUCCESS / FAILED)

Stored in:

```
serving/logging.db
```

---

## 🧠 Model

⚠️ The trained model file is **not included** due to size limits.

### To use the API:

* Place your model here:

```
E1/Model/model.pth
```

---

## 📦 Requirements

Main dependencies:

* fastapi
* uvicorn
* torch
* numpy
* pandas
* psutil
* pydantic

---


## 🚀 Future Improvements

* Dashboard for monitoring (Streamlit / Grafana)
* Model versioning
* Async processing
* Docker deployment
