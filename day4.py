import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split

# Load Final Dataset
df = pd.read_csv(r"C:\Users\shrub\OneDrive\Desktop\fake job detection\dataset\final_dataset.csv")

# Features and Target
X = df["text"]
y = df["fraudulent"]

# TF-IDF Vectorization
vectorizer = TfidfVectorizer(stop_words="english", max_features=5000)

X = vectorizer.fit_transform(X)

print("TF-IDF Completed Successfully!")

print("Feature Matrix Shape:", X.shape)

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("Training Data :", X_train.shape)
print("Testing Data  :", X_test.shape)
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Train Model
model = LogisticRegression(
    max_iter=1000,
    class_weight="balanced",
    random_state=42
)

model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)

print("\n✅ Model Trained Successfully!")

print(f"\nAccuracy : {accuracy*100:.2f}%")

print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))

print("\nConfusion Matrix:\n")
print(confusion_matrix(y_test, y_pred))
print("\nFraudulent Value Counts:")
print(df["fraudulent"].value_counts())
import joblib

joblib.dump(model, "fake_job_model.pkl")
joblib.dump(vectorizer, "tfidf_vectorizer.pkl")

print("\n✅ New Model Saved Successfully!")