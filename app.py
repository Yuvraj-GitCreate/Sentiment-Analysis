import streamlit as st
import joblib

model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")
mapping = joblib.load("mapping.pkl")

st.title("Sentiment Analysis App 😊")

# Input
text = st.text_input("Enter your text:")

# Predict if button clicked OR Enter pressed
if text:
    if st.button("Predict") or st.session_state.get("enter_pressed", True):
        
        vec = vectorizer.transform([text])
        result = int(model.predict(vec)[0])
        emotion = mapping.get(result, "Unknown")

        st.success(f"Emotion: {emotion}")