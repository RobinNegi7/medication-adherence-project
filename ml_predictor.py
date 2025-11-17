# backend/ml_predictor.py
import joblib
import pandas as pd
import os

MODEL_PATH = os.path.join(os.path.dirname(__file__), "..", "models", "adherence_model.joblib")

payload = joblib.load(MODEL_PATH)
model = payload["model"]
columns = payload["columns"]

def predict_next_dose(data: dict):
    """
    data example:
    {
      "time_of_day": "evening",
      "medication_type": "insulin",
      "missed_doses_history": 2,
      "user_activity": 4
    }
    returns: { probability: float, prediction: "likely to miss"/"likely to take on time" }
    """
    df = pd.DataFrame([data])
    df = pd.get_dummies(df)
    # ensure same columns as training
    for col in columns:
        if col not in df.columns:
            df[col] = 0
    df = df[columns]
    prob = float(model.predict_proba(df)[0][1])
    label = "likely to miss" if prob >= 0.5 else "likely to take on time"
    return {"probability": round(prob, 3), "prediction": label}
