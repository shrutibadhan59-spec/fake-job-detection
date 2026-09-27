import streamlit as st
from predictor import predict_job
from styles import load_css

st.set_page_config(
    page_title="Fake Job Detection System",
    page_icon="💼",
    layout="wide",
)

st.markdown(load_css(), unsafe_allow_html=True)
# ==========================
# Sidebar
# ==========================

st.sidebar.title("💼 Fake Job Detection")

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Home",
        "🔍 Predict Job",
        "📊 Dashboard",
        "📈 Model Performance",
        "📜 Prediction History",
        "🤖 AI Workflow",
        "🚀 Future Scope",
        "👩‍💻 About Developer"
    ]
)

st.sidebar.markdown("---")

st.sidebar.success("AI Powered Detection System")

st.sidebar.markdown("""
### 🛠 Technologies

✅ Python

✅ Streamlit

✅ Machine Learning

✅ TF-IDF

✅ Logistic Regression

✅ MySQL
""")

if page == "🏠 Home":

    st.title("💼 Fake Job Detection System")

    st.markdown("---")

    st.success("🚀 Version 3.0 Started Successfully")

    st.write(
        "Welcome to the Professional AI Powered Fake Job Detection System."
    )

    st.markdown("## 🌟 Features")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.success("🤖 AI Prediction")

    with col2:
        st.info("📊 Dashboard")

    with col3:
        st.warning("🛡 Scam Detection")

        st.markdown("---")

    st.subheader("🎯 Objective")

    st.write("""
This system uses Artificial Intelligence and Machine Learning
to detect whether a job posting is Genuine or Fake.

It analyses job descriptions using NLP and Logistic Regression
to protect job seekers from recruitment scams.
""")

elif page == "🔍 Predict Job":

    st.title("🔍 Fake Job Prediction")
    job = st.text_area(
        "Paste Job Description",
        height=250
    )

    if st.button("🚀 Predict Job"):

        if job.strip() == "":
            st.warning("Please enter a Job Description.")

        else:

            result, confidence, risk, flags, score = predict_job(job)
            if result == "Fake":
                st.error("❌ Fake Job Detected")
            else:
                st.success("✅ Real Job Posting")

            col1, col2 = st.columns(2)

            with col1:
                st.metric("Confidence", f"{confidence:.2f}%")

            with col2:
                st.metric("Risk", risk)
    