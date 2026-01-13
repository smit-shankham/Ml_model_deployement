from fastapi import FastAPI
from backend.schemas import HouseFeatures
from backend.predict import predict_price

app = FastAPI(
    title="House Price Prediction API",
    version="1.0"
)

@app.get("/")
def health():
    return {"status": "API running"}

@app.post("/predict")
def predict(data: HouseFeatures):
    return predict_price(data)
