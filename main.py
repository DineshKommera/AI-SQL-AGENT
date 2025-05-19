import openai
from dotenv import load_dotenv
import os
from agent import agent_graph
from langchain.chat_models import ChatOpenAI

# Load environment variables from .env file
load_dotenv()

# Set your OpenAI API key from the environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

# Initialize your agent or other components
llm = ChatOpenAI(model="gpt-4", temperature=0)

print("Agent is ready. Type your request.")
while True:
    user_input = input(">>> ")
    if user_input.lower() in ['exit', 'quit']:
        break

    try:
        result = agent_graph.invoke({"input": user_input})
        print(result.get("output", "No response"))
    except Exception as e:
        print("Error:", e)
 