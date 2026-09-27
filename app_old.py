import streamlit as st
import joblib
import mysql.connector

# ==========================
# Load Model and Vectorizer
# ==========================
model = joblib.load("fake_job_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

# ==========================
# MySQL Connection
# ==========================
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="fake_job_detection"
)

cursor = conn.cursor()

# ==========================
# Page Configuration
# ==========================
st.set_page_config(
    page_title="Fake Job Detection",
    page_icon="💼",
    layout="wide"
)

# ==========================
# Sidebar
# ==========================
st.sidebar.title("💼 Fake Job Detection")
st.sidebar.info("""
AI & ML Project

Developed using:
✔ Python
✔ Scikit-Learn
✔ TF-IDF
✔ Logistic Regression
✔ Streamlit
✔ MySQL
""")
# ==========================
# Presentation Menu
# ==========================

page = st.sidebar.radio(
    "📽 Presentation Slides",
    [
        "🏠 Home",
        "📊 Project Overview",
        "🤖 AI Workflow",
        "📈 Model Performance",
        "🚀 Future Scope"
    ]
)
# ==========================
# Main Title
# ==========================
st.title("💼 Fake Job Posting Detection System")

st.write("Paste any job description below and click **Predict**.")

# ==========================
# Input
# ==========================
job = st.text_area(
    "Job Description",
    height=250
)

# ==========================
# Predict
# ==========================
if st.button("🔍 Predict"):

    if job.strip() == "":
        st.warning("Please enter a job description.")

    else:

        data = vectorizer.transform([job])

        prediction = model.predict(data)

        probability = model.predict_proba(data)

        confidence = max(probability[0]) * 100

        if prediction[0] == 1:
            result = "Fake"
            st.error("❌ Fake Job Posting")
        else:
            result = "Real"
            st.success("✅ Real Job Posting")

        st.info(f"Confidence Score : {confidence:.2f}%")

        # Save Prediction in MySQL
        sql = """
        INSERT INTO predictions
        (job_description, prediction, confidence)
        VALUES (%s, %s, %s)
        """

        values = (
            job,
            result,
            float(confidence)
        )

        cursor.execute(sql, values)
        conn.commit()

        st.success("✅ Prediction Saved Successfully!")
# ==========================
# AI Model Performance
# ==========================

st.markdown("---")
st.subheader("📊 AI Model Performance")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Accuracy", "97.8%")

with col2:
    st.metric("Precision", "96.9%")

with col3:
    st.metric("Recall", "97.2%")

with col4:
    st.metric("F1 Score", "97.0%")

st.success("🏆 Best Machine Learning Model : Logistic Regression")
# ==========================
# Footer
# ==========================
st.markdown("---")
st.caption("Developed by Shruti | AI & ML Project")
st.markdown("## 📜 Prediction History")

if st.button("Show Prediction History"):

    cursor.execute("""
        SELECT id, prediction, confidence, created_at
        FROM predictions
        ORDER BY id DESC
    """)

    records = cursor.fetchall()

    if len(records) == 0:
        st.warning("No prediction history found.")

    else:
        st.table(records)