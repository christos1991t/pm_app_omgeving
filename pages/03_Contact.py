import streamlit as st
from send_emai import send_email

st.header("Contact")

with st.form(key='my_form'):
    user_mail = st.text_input("E-mail address")
    raw_message = st.text_area("Jouw bericht")
    message = f"""\
Subject: New mail from {user_mail}

From: {user_mail}
{raw_message}
"""
    button = st.form_submit_button("Sturen")
    if button:
        send_email(message)
        st.info("E-mail vesrtuurd")
