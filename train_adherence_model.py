# backend/train_adherence_model.py
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import joblib
import os

def generate_dataset(n=1500, seed=42):
    np.random.seed(seed)
    time_of_day = np.random.choice(["morning", "afternoon", "evening"], n)
    med_type = np.random.choice(["bp", "insulin", "painkiller", "vitamin"], n)
    missed_hist = np.random.poisson(1.0, n)
    activity_level = np.random.randint(1, 11, n)
    df = pd.DataFrame({
        "time_of_day": time_of_day,
        "medication_type": med_type,
        "missed_doses_history": missed_hist,
        "user_activity": activity_level
    })
    df = pd.get_dummies(df, columns=["time_of_day", "medication_type"], drop_first=True)
    prob = 0.3 + 0.1 * missed_hist - 0.02 * activity_level
    prob = np.clip(prob, 0.05, 0.95)
    y = (np.random.rand(n) < prob).astype(int)
    df["target"] = y
    return df

df = generate_dataset()
X = df.drop("target", axis=1)
y = df["target"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier(n_estimators=150, random_state=42)
model.fit(X_train, y_train)

print("Accuracy:", accuracy_score(y_test, model.predict(X_test)))
print("Classification Report:\n", classification_report(y_test, model.predict(X_test)))

os.makedirs("models", exist_ok=True)
joblib.dump({"model": model, "columns": X.columns.tolist()}, "models/adherence_model.joblib")
print("✅ Model saved at models/adherence_model.joblib")
