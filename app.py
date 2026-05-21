import streamlit as st
import firebase_admin
from firebase_admin import credentials, db
import time

# -------------------------------
# Firebase INIT (safe check)
# -------------------------------
if not firebase_admin._apps:
    cred = credentials.Certificate("serviceAccountKey (2).json")

    firebase_admin.initialize_app(cred, {
        "databaseURL": https://mini-talker-default-rtdb.firebaseio.com/
    })

chat_ref = db.reference("mini_talker_messages")

# -------------------------------
# UI
# -------------------------------
st.set_page_config(page_title="Mini Talker 💬")
st.title("💬 Mini Talker - WhatsApp Style Chat")

# -------------------------------
# USER INPUT
# -------------------------------
user = st.text_input("Your Name")
message = st.text_input("Message")

if st.button("Send"):
    if user and message:
        data = {
            "user": user,
            "message": message,
            "time": str(time.strftime("%H:%M:%S"))
        }
        chat_ref.push(data)
        st.success("Message sent!")

# -------------------------------
# LOAD MESSAGES
# -------------------------------
st.subheader("Chat Messages")

messages = chat_ref.get()

if messages:
    for key in messages:
        msg = messages[key]
        st.write(f"**{msg['user']}** ({msg['time']}): {msg['message']}")
else:
    st.info("No messages yet")
