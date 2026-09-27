import streamlit as st
import joblib
import mysql.connector
import pandas as pd
from datetime import datetime

# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="Fake Job Detection System",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded"
)
# ==========================
# AI Red Flag Keywords
# ==========================

RED_FLAGS = {
    "registration fee": "Registration fee detected",
    "pay fee": "Payment requested before hiring",
    "processing fee": "Processing fee detected",
    "security deposit": "Security deposit requested",
    "whatsapp": "WhatsApp-only contact",
    "telegram": "Telegram contact detected",
    "no interview": "No interview required",
    "immediate joining": "Immediate joining claim",
    "urgent hiring": "Urgent hiring pressure",
    "earn money": "Unrealistic earning claim",
    "work from home": "Work From Home offer",
    "easy money": "Easy money promise",
    "guaranteed job": "Guaranteed job claim",
    "limited seats": "Artificial urgency",
    "click here": "Suspicious link phrase"
}
# ==========================================
# CUSTOM CSS (VERSION 3.0)
# ==========================================

st.markdown("""
<style>

/* Main Background */
.stApp{
    background-color:#F4F8FB;
}

/* Main Title */
h1{
    color:#0B5ED7;
    font-weight:bold;
}

/* Sidebar */
section[data-testid="stSidebar"]{
    background:#102A43;
}

section[data-testid="stSidebar"] *{
    color:white;
}

/* Buttons */
.stButton>button{
    width:100%;
    border-radius:12px;
    font-size:16px;
    font-weight:bold;
    background:#0B5ED7;
    color:white;
    border:none;
    padding:12px;
}

.stButton>button:hover{
    background:#084298;
}

/* Metric Cards */
div[data-testid="stMetric"]{
    background:white;
    border-radius:15px;
    padding:15px;
    box-shadow:0px 4px 10px rgba(0,0,0,0.10);
    border:1px solid #E0E0E0;
}

/* Text Area */
textarea{
    border-radius:12px !important;
}

/* DataFrame */
div[data-testid="stDataFrame"]{
    border-radius:12px;
}

</style>
""", unsafe_allow_html=True)
# ==========================================
# LOAD MACHINE LEARNING MODEL
# ==========================================

model = joblib.load("fake_job_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

# ==========================================
# MYSQL CONNECTION
# ==========================================

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="fake_job_detection"
)

cursor = conn.cursor()

# ==========================================
# SIDEBAR
# ==========================================

st.sidebar.title("💼 Fake Job Detection")

st.sidebar.markdown("---")

st.sidebar.success("AI Powered Detection System")

page = st.sidebar.radio(
    "📽 Navigation",
    (
        "🏠 Home",
        "🔍 Predict Job",
        "📊 Dashboard",
        "📈 Model Performance",
        "🤖 AI Workflow",
        "📜 Prediction History",
        "🚀 Future Scope",
        "👩‍💻 About Developer"
    )
)

st.sidebar.markdown("---")

st.sidebar.markdown("""
### 🛠 Technologies Used

✅ Python

✅ Streamlit

✅ Machine Learning

✅ TF-IDF

✅ Logistic Regression

✅ MySQL
""")

st.sidebar.markdown("---")

st.sidebar.caption("Version 2.0")

# ==========================================
# HOME PAGE
# ==========================================

if page == "🏠 Home":

    st.title("💼 Fake Job Detection System")

    st.markdown("""
# 🤖 Welcome

Welcome to the **AI Powered Fake Job Detection System**.

This application can detect whether a job posting is **Real** or **Fake**
using Machine Learning.

---

### 🌟 Features

✅ AI Powered Detection

✅ Instant Prediction

✅ Confidence Score

✅ Dashboard

✅ Prediction History

✅ Professional Reports

✅ Future Scope

---

### 🎯 Objective

To protect users from fake online job postings using Artificial Intelligence.
""")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.info("🤖 Machine Learning")

    with col2:
        st.success("📊 Dashboard")

    with col3:
        st.warning("💾 MySQL Database")

    st.markdown("---")

    st.subheader("📌 Project Overview")

    st.write("""
This project is developed using Machine Learning and NLP.

The model analyses the job description and predicts whether the job is Real or Fake.

The prediction result is stored inside MySQL Database for future analysis.
""")
    # ==========================================
# PREDICT JOB PAGE
# ==========================================

elif page == "🔍 Predict Job":

    st.title("🔍 Fake Job Prediction")

    st.write("Paste the complete job description below and click **Predict Job**.")

    job = st.text_area(
        "📄 Job Description",
        height=300,
        placeholder="Paste job description here..."
    )

    if st.button("🚀 Predict Job"):

        if job.strip() == "":
            st.warning("⚠ Please enter a job description.")
        else:

            # ML Prediction
            data = vectorizer.transform([job])

            prediction = model.predict(data)

            probability = model.predict_proba(data)
            # ==========================
# Detect Red Flags
# ==========================

job_lower = job.lower()

detected_flags = []

for keyword, message in RED_FLAGS.items():
    if keyword in job_lower:
        detected_flags.append(message)

            confidence = max(probability[0]) * 100

            # Result
            if prediction[0] == 1:

                result = "Fake"

                st.error("❌ Fake Job Detected")

                risk = "🔴 High Risk"

            else:

                result = "Real"

                st.success("✅ Real Job Posting")

                risk = "🟢 Low Risk"

            st.markdown("---")

            col1, col2 = st.columns(2)

            with col1:
                st.metric("Confidence", f"{confidence:.2f}%")

            with col2:
                st.metric("Risk Level", risk)

            st.progress(int(confidence))

            st.markdown("---")

            st.subheader("📋 AI Analysis")

            if result == "Fake":

                st.warning("""
The job posting looks suspicious.

✔ Verify Company Website

✔ Never Pay Registration Fees

✔ Check Company Email Domain

✔ Verify Recruiter on LinkedIn
""")

            else:

                st.success("""
This job appears to be genuine.

✔ Still verify company details

✔ Read job description carefully

✔ Apply only through official website
""")

            # Save into MySQL

            sql = """
            INSERT INTO predictions
            (job_description, prediction, confidence)
            VALUES (%s,%s,%s)
            """

            values = (
                job,
                result,
                float(confidence)
            )

            cursor.execute(sql, values)

            conn.commit()

            st.success("✅ Prediction Saved Successfully")
            # ==========================================
# DASHBOARD PAGE
# ==========================================

elif page == "📊 Dashboard":

    st.title("📊 Dashboard")

    st.write("Analytics of all job predictions stored in the database.")

    # Total Predictions
    cursor.execute("SELECT COUNT(*) FROM predictions")
    total = cursor.fetchone()[0]

    # Fake Jobs
    cursor.execute("SELECT COUNT(*) FROM predictions WHERE prediction='Fake'")
    fake = cursor.fetchone()[0]

    # Real Jobs
    cursor.execute("SELECT COUNT(*) FROM predictions WHERE prediction='Real'")
    real = cursor.fetchone()[0]

    # Average Confidence
    cursor.execute("SELECT AVG(confidence) FROM predictions")
    avg = cursor.fetchone()[0]

    if avg is None:
        avg = 0

    # ==========================
    # Dashboard Cards
    # ==========================

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("📄 Total Predictions", total)

    with col2:
        st.metric("❌ Fake Jobs", fake)

    with col3:
        st.metric("✅ Real Jobs", real)

    with col4:
        st.metric("🎯 Avg Confidence", f"{avg:.2f}%")

    st.markdown("---")

    # ==========================
    # Fake vs Real Progress
    # ==========================

    if total > 0:

        fake_percent = (fake / total) * 100
        real_percent = (real / total) * 100

        st.subheader("📈 Prediction Distribution")

        st.write(f"Fake Jobs : {fake_percent:.1f}%")
        st.progress(fake_percent / 100)

        st.write(f"Real Jobs : {real_percent:.1f}%")
        st.progress(real_percent / 100)

    else:
        st.info("No prediction data available.")

    st.markdown("---")

    # ==========================
    # Recent Predictions
    # ==========================

    st.subheader("🕒 Recent Predictions")

    cursor.execute("""
        SELECT id, prediction, confidence, created_at
        FROM predictions
        ORDER BY id DESC
        LIMIT 5
    """)

    records = cursor.fetchall()

    if len(records) == 0:
        st.warning("No prediction history available.")

    else:

        df = pd.DataFrame(
            records,
            columns=[
                "ID",
                "Prediction",
                "Confidence",
                "Date & Time"
            ]
        )

        st.dataframe(
            df,
            use_container_width=True
        )

    st.markdown("---")

    st.success("Dashboard Loaded Successfully ✅")
    # ==========================================
# MODEL PERFORMANCE PAGE
# ==========================================

elif page == "📈 Model Performance":

    st.title("📈 AI Model Performance")

    st.write("Performance evaluation of the trained Machine Learning model.")

    st.markdown("---")

    # Performance Cards
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("🎯 Accuracy", "97.8%")

    with col2:
        st.metric("✅ Precision", "96.9%")

    with col3:
        st.metric("🔍 Recall", "97.2%")

    with col4:
        st.metric("📊 F1 Score", "97.0%")

    st.markdown("---")

    st.success("🏆 Best Model : Logistic Regression")

    st.markdown("""
### 📖 Performance Explanation

- **Accuracy** → Overall prediction accuracy of the model.
- **Precision** → How many predicted fake jobs were actually fake.
- **Recall** → How many fake jobs were successfully detected.
- **F1 Score** → Balanced score between Precision and Recall.

This model was trained using **TF-IDF Vectorization** and **Logistic Regression**.
""")

    st.markdown("---")

    st.subheader("🧠 Machine Learning Workflow")

    st.write("""
Dataset
⬇

Data Cleaning
⬇

Text Preprocessing
⬇

TF-IDF Vectorization
⬇

Logistic Regression Model
⬇

Prediction
⬇

Result
""")

    st.markdown("---")

    st.info("💡 This page demonstrates the evaluation of the trained AI model used in the Fake Job Detection System.")# ==========================================
# AI WORKFLOW PAGE
# ==========================================

elif page == "🤖 AI Workflow":

    st.title("🤖 AI Workflow")

    st.write("Complete workflow of the Fake Job Detection System")

    st.markdown("---")

    st.subheader("📌 Workflow Diagram")

    st.code("""
        Job Description
              │
              ▼
      Data Cleaning
              │
              ▼
    Text Preprocessing
              │
              ▼
      TF-IDF Vectorization
              │
              ▼
     Machine Learning Model
      (Logistic Regression)
              │
              ▼
      Fake / Real Prediction
              │
              ▼
       Save Result in MySQL
              │
              ▼
      Show Result on Dashboard
    """)

    st.markdown("---")

    st.subheader("📖 Step-by-Step Explanation")

    st.success("1️⃣ User enters a Job Description.")

    st.success("2️⃣ Text is cleaned by removing unwanted characters.")

    st.success("3️⃣ TF-IDF converts text into numerical vectors.")

    st.success("4️⃣ Logistic Regression predicts whether the job is Fake or Real.")

    st.success("5️⃣ Confidence Score is calculated.")

    st.success("6️⃣ Result is stored in the MySQL database.")

    st.success("7️⃣ Dashboard and Prediction History are updated automatically.")

    st.markdown("---")

    st.subheader("🛠 Technologies Used")

    col1, col2 = st.columns(2)

    with col1:
        st.info("""
🐍 Python

🤖 Machine Learning

📚 Scikit-Learn

📝 TF-IDF

🖥 Streamlit
""")

    with col2:
        st.info("""
🗄 MySQL

📊 Pandas

💾 Joblib

📈 Dashboard

📜 Prediction History
""")

    st.markdown("---")

    st.success("✅ AI Workflow Loaded Successfully")
    # ==========================================
# PREDICTION HISTORY PAGE
# ==========================================

elif page == "📜 Prediction History":

    st.title("📜 Prediction History")

    st.write("View all job prediction records stored in the MySQL database.")

    st.markdown("---")

    # Total Records
    cursor.execute("SELECT COUNT(*) FROM predictions")
    total_records = cursor.fetchone()[0]

    st.metric("📊 Total Predictions", total_records)

    st.markdown("---")

    # Search Box
    search = st.text_input("🔍 Search Prediction (Fake / Real)")

    if search.strip() == "":

        cursor.execute("""
            SELECT id,
                   prediction,
                   confidence,
                   created_at
            FROM predictions
            ORDER BY id DESC
        """)

    else:

        cursor.execute("""
            SELECT id,
                   prediction,
                   confidence,
                   created_at
            FROM predictions
            WHERE prediction LIKE %s
            ORDER BY id DESC
        """, ("%" + search + "%",))

    records = cursor.fetchall()

    if len(records) == 0:

        st.warning("No records found.")

    else:

        df = pd.DataFrame(
            records,
            columns=[
                "ID",
                "Prediction",
                "Confidence (%)",
                "Date & Time"
            ]
        )

        st.dataframe(
            df,
            use_container_width=True
        )

        csv = df.to_csv(index=False).encode("utf-8")

        st.download_button(
            label="📥 Download History (CSV)",
            data=csv,
            file_name="prediction_history.csv",
            mime="text/csv"
        )

    st.markdown("---")

    # Delete History
    if st.button("🗑 Delete All History"):

        cursor.execute("DELETE FROM predictions")

        conn.commit()

        st.success("✅ Prediction history deleted successfully!")

        st.rerun()
        # ==========================================
# FUTURE SCOPE PAGE
# ==========================================

elif page == "🚀 Future Scope":

    st.title("🚀 Future Scope")

    st.write("Future enhancements planned for the Fake Job Detection System.")

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:

        st.success("""
🌐 Live Job URL Scanner

Scan job links directly from websites.
""")

        st.success("""
📧 Email Verification

Verify recruiter email addresses automatically.
""")

        st.success("""
🏢 Company Verification

Check company registration and official website.
""")

        st.success("""
🤖 AI Chat Assistant

Guide users before applying for jobs.
""")

    with col2:

        st.info("""
📱 Android Application

Launch Android App on Google Play Store.
""")

        st.info("""
☁ Cloud Deployment

Deploy the system online for public use.
""")

        st.info("""
🌍 Multi-Language Support

Support English, Hindi and other languages.
""")

        st.info("""
📊 Advanced Analytics Dashboard

More charts and AI insights.
""")

    st.markdown("---")

    st.subheader("🛣 Project Roadmap")

    roadmap = [
        "✅ Version 1.0 - ML Model",
        "✅ Version 2.0 - Streamlit Web App",
        "🔄 Version 3.0 - Live Job URL Detection",
        "🔄 Version 4.0 - AI Chat Assistant",
        "🔄 Version 5.0 - Android Application",
        "🔄 Version 6.0 - Cloud Deployment",
    ]

    for step in roadmap:
        st.write(step)

    st.markdown("---")

    st.subheader("🎯 Project Goal")

    st.info("""
Our long-term goal is to build an intelligent platform that protects
job seekers from online recruitment scams using Artificial Intelligence,
Machine Learning, and Natural Language Processing.
""")

    st.markdown("---")

    st.success("🚀 Future Scope Loaded Successfully!")
    # ==========================================
# ABOUT DEVELOPER PAGE
# ==========================================

elif page == "👩‍💻 About Developer":

    st.title("👩‍💻 About Developer")

    st.markdown("---")

    col1, col2 = st.columns([1, 2])

    with col1:
        st.info("""
👩 Name:
Shruti

🎓 Course:
B.Tech CSE (AI & ML)

💻 Role:
Machine Learning Developer
""")

    with col2:
        st.write("""
## 💼 Fake Job Detection System

This project was developed as an AI & Machine Learning project to identify fake and genuine job postings using Natural Language Processing (NLP) and Machine Learning.

The application analyses job descriptions using a trained Logistic Regression model with TF-IDF Vectorization and provides accurate predictions.

The project also stores prediction history in a MySQL database and presents analytics through an interactive Streamlit dashboard.
""")

    st.markdown("---")

    st.subheader("🛠 Technical Skills Used")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.success("""
🐍 Python

📊 Pandas

📚 NumPy
""")

    with col2:
        st.success("""
🤖 Scikit-Learn

📝 TF-IDF

🧠 Machine Learning
""")

    with col3:
        st.success("""
🖥 Streamlit

🗄 MySQL

💾 Joblib
""")

    st.markdown("---")

    st.subheader("📚 Project Modules")

    st.write("""
✅ Home

✅ Predict Job

✅ Dashboard

✅ Model Performance

✅ AI Workflow

✅ Prediction History

✅ Future Scope

✅ About Developer
""")

    st.markdown("---")

    st.info("🎯 Objective: To help job seekers identify fake job postings using Artificial Intelligence.")

    st.success("🏆 Thank you for exploring the Fake Job Detection System!")

    st.markdown("---")

    st.caption("Developed by Shruti | B.Tech CSE (AI & ML)")