import requests
import streamlit as st

def get_google_genai_response(input_text: str) -> str:
    response = requests.post(
        "http://localhost:8000/essay/invoke",
        json={"topic": input_text}
    )
    return response.json()["result"]

st.title("LangChain Google Gemini Chatbot")

input_text = st.text_area(
    "Enter your question here:",
    height=100
)

if input_text:
    st.write(get_google_genai_response(input_text))
