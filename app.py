import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Lica-Pro AI assistant genai-based")
state = st.session_state
if "user_messages" not in state:
  state.memory = []
  state.user_messages = []
  state.ai_messages = []
with st.sidebar:
  st.title("Type your API key to start")
  st.write("You can get those in https://aistudio.google.com/app/api-keys")
  api_key = st.text_input("Type here")
  submit = st.button("Submit")
  model = st.selectbox(
    "Select a model",
    options=['gemini-2.5-pro', 'gemini-3.1-flash', 'gemini-2.5-flash', 'gemini-3.1-flash-lite', 'gemini-2.5-flash-lite']
  )
  if api_key:
    if submit:
      st.success("Now you can close this sidebar to chat!")
