from dotenv import load_dotenv
import chainlit as cl
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage

# Load environment variables from .env
load_dotenv()

# Initialize Groq model
chat = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0.3,
)

# Chainlit chat handler
@cl.on_message
async def handle_message(message: cl.Message):
    user_input = message.content

    # Generate response from Groq
    response = chat.invoke([HumanMessage(content=user_input)])

    # Send response back to Chainlit UI
    await cl.Message(content=response.content).send()
