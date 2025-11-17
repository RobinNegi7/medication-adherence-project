# backend/recommendation_system.py
def get_health_recommendations(medication_type: str):
    medication_type = (medication_type or "").lower()
    recommendations = {
        "bp": {
            "diet": "Reduce salt intake; include potassium-rich foods.",
            "sleep": "Keep 7–8 hours of sleep.",
            "doctor": "Consult cardiologist if BP > 140/90."
        },
        "insulin": {
            "diet": "Avoid sugary foods; increase fiber.",
            "sleep": "Keep consistent sleep schedule.",
            "doctor": "Contact endocrinologist if glucose spikes."
        },
        "painkiller": {
            "diet": "Stay hydrated; avoid alcohol.",
            "sleep": "Rest and avoid strenuous activity.",
            "doctor": "If pain persists >3 days, see a physician."
        },
        "vitamin": {
            "diet": "Eat balanced meals with fruits & vegetables.",
            "sleep": "Maintain regular sleep.",
            "doctor": "Routine check-up recommended."
        }
    }
    return recommendations.get(medication_type, {
        "diet": "Maintain a balanced diet.",
        "sleep": "Ensure adequate rest.",
        "doctor": "Consult your provider if concerned."
    })
