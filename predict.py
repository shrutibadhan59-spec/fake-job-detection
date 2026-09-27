import joblib

# Load Model and Vectorizer
model = joblib.load("fake_job_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

print("====== Fake Job Detection ======\n")

job = input("Enter Job Description:\n\n")

job_vector = vectorizer.transform([job])

prediction = model.predict(job_vector)

print("\n========================")

if prediction[0] == 1:
    print("❌ Fake Job Posting")
else:
    print("✅ Real Job Posting")