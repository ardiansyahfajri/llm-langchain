import streamlit as st
import requests

st.set_page_config(page_title="AI Generator", layout="centered")

st.title("📝 AI Essay & Poem Generator")

tab1, tab2 = st.tabs(["📄 Essay (OpenAI)", "🖋️ Poem (Anthropic)"])

API_URL = "http://localhost:8000"

with tab1:
    st.header("Generate an Essay")
    topic = st.text_input("Essay Topic", key="essay")
    if st.button("Generate Essay"):
        if topic.strip():
            with st.spinner("Generating essay..."):
                response = requests.post(f"{API_URL}/essay", json={"topic": topic})
                if response.ok:
                    st.success("Essay generated:")
                    st.write(response.json()["essay"])
                else:
                    st.error("Failed to generate essay. Please check the server.")
        else:
            st.warning("Please enter a topic.")

with tab2:
    st.header("Generate a Poem")
    topic = st.text_input("Poem Topic", key="poem")
    if st.button("Generate Poem"):
        if topic.strip():
            with st.spinner("Generating poem..."):
                response = requests.post(f"{API_URL}/poem", json={"topic": topic})
                if response.ok:
                    st.success("Poem generated:")
                    st.write(response.json()["poem"])
                else:
                    st.error("Failed to generate poem. Please check the server.")
        else:
            st.warning("Please enter a topic.")
