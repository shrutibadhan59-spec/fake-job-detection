import pandas as pd
import joblib

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Load Dataset
df = pd.read_csv(r"C:\Users\shrub\OneDrive\Desktop\fake job detection\dataset\final_dataset.csv")

# Features and Target
X = df["text"]
y = df["fraudulent"]

# TF-IDF
vectorizer = TfidfVectorizer(stop_words="english", max_features=5000)
X = vectorizer.fit_transform(X)

# Split Data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train Model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Save Model
joblib.dump(model, "fake_job_model.pkl")

# Save Vectorizer
joblib.dump(vectorizer, "tfidf_vectorizer.pkl")

print("✅ Model Saved Successfully!")
print("✅ Vectorizer Saved Successfully!")