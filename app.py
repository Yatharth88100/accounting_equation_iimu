# app.py
import streamlit as st
from logic import generate_question

st.set_page_config(page_title="Accounting Equation Tutor", layout="centered")

st.title("📘 Accounting Equation Practice Tutor")
st.write("Generates **new questions with solutions** using accounting rules")

topic = st.selectbox(
    "Choose a topic",
    [
        "Capital Introduction",
        "Asset Purchase (Cash)",
        "Asset Purchase (Credit)",
        "Expense Payment",
        "Sales (Cash)",
        "Sales (Credit)"
    ]
)

if st.button("Generate Question"):
    question, solution = generate_question(topic)

    st.subheader("🧠 Question")
    st.info(question)

    st.subheader("✅ Solution")
    st.success(solution)
