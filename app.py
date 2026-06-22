import streamlit as st
from google import genai
st.set_page_config(
    page_title="Lica-pro AI model Gemini-based"
    )
state = st.session_state
if "user_messages" not in state:
    state.memory = []
    state.user_messages = []
    state.ai_messages = []
st.title("Lica-Pro AI model Gemini-based")
with st.sidebar:
    st.title("Enter your API key to start chatting")
    st.write("You can get those in https://aistudio.google.com/app/api-keys")
    api_key = st.text_input("Type here:", type="password")
    model = st.selectbox(
      "Chose a model: ",
      ["gemini-2.5-pro", "gemini-3.5-flash", "gemini-2.5-flash", "gemini-3.1-flash-lite", "gemini-2.5-flash-lite"],
      )
    submit_key = st.button("Submit")
    if submit_key:
        if api_key:
          st.success("You typed your API key so now you can now start chatting but make sure you typed it correct")
        else:
          st.error("Please type your API key to start chatting")
if api_key:
  client = genai.Client(api_key=api_key)
  message = st.chat_input("Ask anything")
  for user_msg, ai_msg in zip(state.user_messages, state.ai_messages):
      st.chat_message("user").write(user_msg)
      st.chat_message("ai").markdown(ai_msg)
  if message:
      state.memory.append(message)
      state.user_messages.append(message)
      st.chat_message("user").write(message)
      try:
        with st.spinner("Thinking..."):
          chat = "\n".join(state.memory)
          response = client.models.generate_content(
          model=model,
          contents=chat
          )
        reply = response.text
        state.memory.append(reply)
      except Exception as e:
          reply = f"An error has occurred: {str(e)}"

      state.ai_messages.append(reply)
      st.chat_message("ai").markdown(reply)
else:
    st.info("Please type your API key inside the sidebar to start chatting")
