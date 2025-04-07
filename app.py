import streamlit as st
from commands import perform_action

st.set_page_config(page_title="Gesture Assistant", layout="centered")
st.title("🖐️ Gesture-Controlled Virtual Assistant")
st.markdown("Select number of fingers to simulate a gesture:")

fingers = st.selectbox("Choose finger count:", [1, 2, 3, 5])

if st.button("Perform Action"):
    perform_action(fingers)
    st.success(f"Performed action for gesture: {fingers} fingers")
