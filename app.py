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
