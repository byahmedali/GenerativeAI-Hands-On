import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

# Get API key
api_key = os.getenv("GEMINI_API_KEY")

# Initialize Gemini model
chat = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.3, google_api_key=api_key)

# Start a loop to chat
print("Chatbot: Hello! Ask me anything. Type 'exit' to stop.")
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        break
    response = chat.invoke([HumanMessage(content=user_input)])
    print("Chatbot: ", response.content)
