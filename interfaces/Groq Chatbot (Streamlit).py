from dotenv import load_dotenv
import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage

# Load environment variables from .env
load_dotenv()

# Initialize Groq model
chat = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0.3,
)

# Set page title
st.title("Groq AI Chatbot")

# Initialize chat history in session state if it doesn't exist
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("What would you like to know?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate response from Groq
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = chat.invoke([HumanMessage(content=prompt)])
            st.markdown(response.content)
            
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response.content})
