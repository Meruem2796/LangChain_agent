from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

messages = [
    HumanMessage(
        content="Tell me a short story about a robot learning to cook."
    )
]

print("Streaming response:\n")

# Stream tokens as they arrive
for chunk in llm.stream(messages):
    print(chunk.content, end="", flush=True)

print("\n\nDone!")
