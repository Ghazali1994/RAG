import streamlit as st
import requests

st.title("Tamil Nadu Govt Assistant")

question = st.text_input("Ask a question")

if question:

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "gemma3:4b",
            "prompt": question,
            "stream": False
        }
    )

    answer = response.json()["response"]

    st.write(answer)
