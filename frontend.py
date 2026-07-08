import streamlit as st
import os
import requests

def invoke_agent(prompt: str) -> int:
    data = dict(
        request = prompt
    )

    response = requests.post("http://127.0.0.1:8000/agent/", json=data)
    return response.status_code


uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    save_path = os.path.join("uploaded_files", uploaded_file.name)
    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    if os.path.exists(save_path):
        st.write("File uploaded!")

prompt = st.chat_input("Say something")
if prompt:
    st.write(f"User has sent the following prompt: {prompt}")
    status_code = invoke_agent(prompt)
    if status_code == 200:
        st.write("Task created!\nDocument created!")
