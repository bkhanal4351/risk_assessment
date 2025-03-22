from fastapi import FastAPI
import joblib
import numpy as np

from fastapi.middleware.cors import CORSMiddleware




app = FastAPI()

# Load the trained model
model = joblib.load("epa_risk_model.pkl")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins (for local development)
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods
    allow_headers=["*"],  # Allows all headers
)

@app.get("/")
def home():
    return {"message": "EPA Risk Assessment API"}


@app.post("/predict/")
def predict_risk(data: dict):
    try:
        input_features = np.array([
            data["chemical_concentration"],
            data["air_quality_index"],
            data["water_toxicity"],
            data["soil_contamination"]
        ]).reshape(1, -1)

        risk_level = model.predict(input_features)[0]
        risk_mapping = {0: "Low", 1: "Moderate", 2: "High"}
        return {"risk_level": risk_mapping[risk_level]}
    except KeyError:
        return {"error": "Invalid input data"}
