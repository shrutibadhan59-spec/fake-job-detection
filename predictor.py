import joblib

RED_FLAGS = {
    "registration fee": 25,
    "processing fee": 25,
    "security deposit": 25,
    "pay fee": 25,
    "whatsapp": 20,
    "telegram": 20,
    "no interview": 15,
    "urgent hiring": 10,
    "immediate joining": 10,
    "work from home": 5,
    "easy money": 20,
    "earn money": 20,
    "guaranteed job": 25,
    "limited seats": 10,
    "click here": 15
}

# Load Model
model = joblib.load("fake_job_model.pkl")

# Load Vectorizer
vectorizer = joblib.load("tfidf_vectorizer.pkl")


def predict_job(job_text):

    data = vectorizer.transform([job_text])

    prediction = model.predict(data)[0]

    probability = model.predict_proba(data)[0]

    confidence = max(probability) * 100

    # Detect Red Flags
    job_lower = job_text.lower()

    detected_flags = []

    risk_score = 0

    for keyword, score in RED_FLAGS.items():
        if keyword in job_lower:
            detected_flags.append(keyword)
            risk_score += score

    risk_score = min(risk_score, 100)

    # Prediction Result
    if prediction == 1:
        result = "Fake"
        risk = "🔴 High Risk"
    else:
        result = "Real"
        risk = "🟢 Low Risk"

    return result, confidence, risk, detected_flags, risk_score