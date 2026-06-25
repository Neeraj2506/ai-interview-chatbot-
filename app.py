import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")

st.title("Neeraj AI Chatbot")

question = st.text_input("Ask me anything")

if question:
    response = model.generate_content(question)
    st.write(response.text)