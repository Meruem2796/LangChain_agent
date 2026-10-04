import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage

# Load environment variables from .env file
load_dotenv()

# Verify the API key is loaded
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError(
        "OPENAI_API_KEY not found. Make sure your .env file exists and contains the key."
    )

# Initialize the Chat LLM
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0,  # 0 = deterministic, 1 = more creative
    max_tokens=500,  # limit response length
)

# Build a list of messages
messages = [
    SystemMessage(
        content="You are a helpful assistant who explains technical concepts simply."
    ),
    HumanMessage(content="What is LangChain in one sentence?"),
]

# Call the model
print("Sending request to OpenAI...")
response = llm.invoke(messages)

# Print the response
print("\nResponse:")
print(response.content)

# Print some metadata
print("\nModel used:", response.response_metadata.get("model_name"))
print("Tokens used:", response.response_metadata.get("token_usage"))
