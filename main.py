import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

llm = ChatGoogleGenerativeAI(
    model = "gemini-2.5-flash",
    google_api_key = "hahaha"
)

if "messages" not in st.session_state:
    st.session_state.messages = []

if "current_mode" not in st.session_state:
    st.session_state.current_mode = "Chatbot"

selected_mode = st.sidebar.radio("Choose mode", ["Chatbot", "Story Generator", "Joke Generator"])

if selected_mode != st.session_state.current_mode:
    st.session_state.messages = []
    st.session_state.current_mode = selected_mode

system_prompts = {
    "Chatbot" : "You are a helpful assistant.",
    "Story Generator" : "You are a creative story writer. Write a creative story according to the prompt or theme given by the user",
    "Joke Generator" : "You are a comedian. Respond only with puns or oneliners to whatever the user says prompts"
}

def get_messages_with_system():
    system = SystemMessage(content=system_prompts[st.session_state.current_mode])
    return [system] + st.session_state.messages

st.title(f"{selected_mode}")


for message in st.session_state.messages:
    if isinstance(message, HumanMessage):
        with st.chat_message("user"):
            st.write(message.content)

    else:
        with st.chat_message("assistant"):
            st.write(message.content)

user_input = st.chat_input("Type your message")

if user_input:
    st.session_state.messages.append(HumanMessage(content= user_input))

    with st.chat_message("user"):
        st.write(user_input)

    response = llm.invoke(get_messages_with_system())
    st.session_state.messages.append(AIMessage(content= response.content))

    with st.chat_message("assistant"):
        st.write(response.content)







