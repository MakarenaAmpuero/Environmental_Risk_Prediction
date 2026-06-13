from fastapi import FastAPI
import joblib
import pandas as pd


app = FastAPI(
    title="Environmental Risk Prediction API"
)


model = joblib.load(
    "environmental_risk_model.joblib"
)


@app.get("/")
def home():
    return {
        "message": "Environmental Risk Prediction API is running"
    }


@app.post("/predict")
def predict(data: dict):

    input_data = pd.DataFrame([data])

    prediction = model.predict(input_data)

    return {
        "risk_prediction": prediction[0]
    }
    