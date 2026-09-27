import streamlit as st
import random
import smtplib
from email.message import EmailMessage
from datetime import datetime
import mysql.connector


def send_otp(receiver_email, otp):

    sender_email = st.secrets["EMAIL_ADDRESS"]
    app_password = st.secrets["EMAIL_APP_PASSWORD"]

    msg = EmailMessage()

    msg["Subject"] = "Fake Job Detection - Login OTP"
    msg["From"] = sender_email
    msg["To"] = receiver_email

    msg.set_content(
        f"""
Hello,

Your OTP for Fake Job Detection is:

{otp}

Please do not share this OTP with anyone.

Regards,
Fake Job Detection Team
"""
    )

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(sender_email, app_password)
        smtp.send_message(msg)


def save_login(email):

    conn = mysql.connector.connect(
        host=st.secrets["MYSQL_HOST"],
        user=st.secrets["MYSQL_USER"],
        password=st.secrets["MYSQL_PASSWORD"],
        database=st.secrets["MYSQL_DATABASE"]
    )

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO users (email)
        VALUES (%s)
        ON DUPLICATE KEY UPDATE email = VALUES(email)
        """,
        (email,)
    )

    cursor.execute(
        """
        INSERT INTO login_history (email, login_time)
        VALUES (%s, %s)
        """,
        (email, datetime.now())
    )

    conn.commit()

    cursor.close()
    conn.close()


def login():

    if "otp" not in st.session_state:
        st.session_state.otp = None

    if "otp_email" not in st.session_state:
        st.session_state.otp_email = None

    if "otp_sent" not in st.session_state:
        st.session_state.otp_sent = False

    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if st.session_state.logged_in:
        return True

    st.title("🔐 Fake Job Detection")

    st.subheader("Login with your Email")

    email = st.text_input(
        "📧 Email Address",
        placeholder="Enter your email address"
    )

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

                st.success(
                    "✅ OTP sent successfully! Check your email."
                )

            except Exception as e:

                st.error("❌ Unable to send OTP.")
                st.error(str(e))

    if st.session_state.otp_sent:

        st.divider()

        st.subheader("🔢 Verify OTP")

        entered_otp = st.text_input(
            "Enter 6-digit OTP",
            max_chars=6,
            type="password"
        )

        if st.button("✅ Verify OTP"):

            if entered_otp == st.session_state.otp:

                try:

                    save_login(st.session_state.otp_email)

                    st.session_state.logged_in = True
                    st.session_state.otp_sent = False

                    st.success("🎉 Login successful!")

                    st.rerun()

                except Exception as e:

                    st.error(
                        "OTP verified, but MySQL save failed."
                    )
                    st.error(str(e))

            else:

                st.error("❌ Incorrect OTP.")

    return False