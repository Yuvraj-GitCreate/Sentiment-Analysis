import streamlit as st
import pickle

# Load files
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))
mapping = pickle.load(open("mapping.pkl", "rb"))

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