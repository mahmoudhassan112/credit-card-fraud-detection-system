FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    && pip install --upgrade pip 

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . . 

RUN mkdir -p E1/Model

WORKDIR /app/serving

EXPOSE 8000

CMD ["uvicorn" , "app:app" ,"--host" , "0.0.0.0","--port" , "8000"]


