import streamlit as st
import requests

st.title("📅 Chat to Book Appointments")

if "messages" not in st.session_state:
    st.session_state.messages = []

def send_message(msg):
    res = requests.post("http://localhost:8000/chat", json={"message": msg})
    return res.json()["response"]

user_input = st.chat_input("Book an appointment...")

if user_input:
    st.session_state.messages.append(("user", user_input))
    bot_reply = send_message(user_input)
    st.session_state.messages.append(("bot", bot_reply))

for sender, msg in st.session_state.messages:
    with st.chat_message(sender):
        st.markdown(msg)
