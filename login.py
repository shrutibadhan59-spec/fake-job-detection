import streamlit as st
import random
import smtplib
from email.message import EmailMessage
from datetime import datetime
import mysql.connector


# ---------------- PAGE SETTINGS ----------------
st.set_page_config(
    page_title="Fake Job Detection - Login",
    page_icon="🔐",
    layout="wide"
)


# ---------------- SESSION STATE ----------------
if "otp" not in st.session_state:
    st.session_state.otp = None

if "otp_email" not in st.session_state:
    st.session_state.otp_email = None

if "otp_sent" not in st.session_state:
    st.session_state.otp_sent = False

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False


# ---------------- FUNCTIONS ----------------

def send_otp(receiver_email, otp):

    sender_email = st.secrets["EMAIL_ADDRESS"]
    app_password = st.secrets["EMAIL_APP_PASSWORD"]

    msg = EmailMessage()

    msg["Subject"] = "Fake Job Detection - Your OTP"
    msg["From"] = sender_email
    msg["To"] = receiver_email

    msg.set_content(
        f"""
Hello,

Your OTP for Fake Job Detection login is:

{otp}

This OTP is valid for this login attempt.

If you did not request this OTP, please ignore this email.

Regards,
Fake Job Detection Team
"""
    )

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(sender_email, app_password)
        smtp.send_message(msg)


def save_login(email):

    connection = mysql.connector.connect(
        host=st.secrets["MYSQL_HOST"],
        user=st.secrets["MYSQL_USER"],
        password=st.secrets["MYSQL_PASSWORD"],
        database=st.secrets["MYSQL_DATABASE"]
    )

    cursor = connection.cursor()

    # Save user
    cursor.execute(
        """
        INSERT INTO users (email)
        VALUES (%s)
        ON DUPLICATE KEY UPDATE email = VALUES(email)
        """,
        (email,)
    )

    # Save login history
    cursor.execute(
        """
        INSERT INTO login_history (email, login_time)
        VALUES (%s, %s)
        """,
        (email, datetime.now())
    )

    connection.commit()

    cursor.close()
    connection.close()


# ---------------- LOGIN UI ----------------

st.title("🔐 Fake Job Detection")

st.subheader("Login with your Email")

email = st.text_input(
    "📧 Email Address",
    placeholder="Enter your email address"
)


# ---------------- SEND OTP ----------------

if st.button("📨 Send OTP"):

    if not email:
        st.error("Please enter your email address.")

    elif "@" not in email or "." not in email:
        st.error("Please enter a valid email address.")

    else:

        otp = str(random.randint(100000, 999999))

        try:

            send_otp(email, otp)

            st.session_state.otp = otp
            st.session_state.otp_email = email
            st.session_state.otp_sent = True

            st.success("OTP sent successfully! Please check your email.")

        except Exception as e:

            st.error("Unable to send OTP.")
            st.error(str(e))


# ---------------- OTP VERIFICATION ----------------

if st.session_state.otp_sent:

    st.divider()

    st.subheader("🔢 Verify OTP")

    entered_otp = st.text_input(
        "Enter the 6-digit OTP",
        max_chars=6,
        type="password"
    )

    if st.button("✅ Verify OTP"):

        if entered_otp == st.session_state.otp:

            try:

                save_login(st.session_state.otp_email)

                st.session_state.logged_in = True
                st.session_state.otp_sent = False

                st.success("Login successful! 🎉")

                st.balloons()

                st.info(
                    f"Logged in as: {st.session_state.otp_email}"
                )

            except Exception as e:

                st.error("OTP verified, but MySQL login history could not be saved.")
                st.error(str(e))

        else:

            st.error("❌ Incorrect OTP. Please try again.")


# ---------------- LOGIN SUCCESS ----------------

if st.session_state.logged_in:

    st.divider()

    st.success("🔓 You are now logged in to Fake Job Detection.")

    st.write(
        "Your email and login date/time have been saved successfully."
    )