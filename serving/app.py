# The Packages we will need for Deployment stage.

import logging
import torch
import numpy as np
from model import ExperimentModel_1
from fastapi import FastAPI
from build_database import cursor , engine
from datetime import datetime
from pydantic import create_model
import time
import uuid 
import psutil 
import os 

# Get the directory of the model

Base_Model_Path = '../E1/Model'

model = ExperimentModel_1()          
model.load_state_dict(torch.load(Base_Model_Path+"/model.pth"))
model.eval()                        

# We check every transaction by BaseModel class

FEATURES = [
    'Time','V1','V2','V3','V4','V5','V6','V7','V8','V9','V10',
    'V11','V12','V13','V14','V15','V16','V17','V18','V19','V20',
    'V21','V22','V23','V24','V25','V26','V27','V28','Amount'
]

Transaction = create_model(
    "Transaction",
    **{feature: (float, ...) for feature in FEATURES}
)

# convert each transaction into tensor 

def to_tensor(transaction: Transaction):
    data = np.array([getattr(transaction, f) for f in FEATURES], dtype=np.float32)
    return torch.tensor(data).unsqueeze(0)

# Create app object first

app = FastAPI()

request_counter = 0
window_start = time.time()


@app.post("/predict")
def predict(transaction: Transaction):

    global request_counter, window_start

    request_id = str(uuid.uuid4())
    start = time.time()
    try:
            request_counter += 1

            elapsed = time.time() - window_start
            throughput = request_counter / max(elapsed, 1e-6)
            client_X  = to_tensor(transaction)

            with torch.no_grad():
                
                output = model(client_X).item()
                
                pred = (output > 0.5)

            latency = (time.time() - start) * 1000

            cpu = psutil.cpu_percent()
            memory = psutil.virtual_memory().percent

            cursor.execute("""
        INSERT INTO inference_logs (
            request_id,
            timestamp,
            probability_output,
            prediction,
            latency_ms,
            throughput_rps,
            cpu_percent,
            memory_percent,
            status,
            error_message
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            request_id,
            datetime.now().isoformat(),
            output,
            pred,
            latency,
            throughput,
            cpu,
            memory,
            "SUCCESS",
            None
        ))

            engine.commit()

            return {
                 
              "label": "Fraud" if pred == 1 else "Normal"
            }

    except Exception as e:

        latency = (time.time() - start) * 1000

        cursor.execute("""
        INSERT INTO inference_logs (
            request_id,
            timestamp,
            latency_ms,
            status,
            error_message
        )
        VALUES (?,?, ?, ?, ?)
        """, (
            request_id,
            datetime.now().isoformat(),
            latency,
            "FAILED",
            str(e)
        ))
        engine.commit()

        return {"error": str(e)}
    
