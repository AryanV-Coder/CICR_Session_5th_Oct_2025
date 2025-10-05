import streamlit as st
import google.generativeai as genai

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
model = genai.GenerativeModel("gemini-2.5-flash",system_instruction="Create a funny 4 line song based on user input. Return output in Hinglish")

st.title("FUNNY SONG CREATOR")

prompt = st.text_input("Enter Your Prompt")
submit = st.button("Send")

if (submit) :
    response = model.generate_content(prompt)
    st.markdown(response.text)