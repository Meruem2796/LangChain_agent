import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from openai import AuthenticationError, RateLimitError, APIConnectionError

load_dotenv()


def call_llm(prompt: str) -> str:
    """Call the LLM with proper error handling."""

    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    messages = [HumanMessage(content=prompt)]

    try:
        response = llm.invoke(messages)
        return response.content

    except AuthenticationError:
        # Wrong or missing API key
        raise ValueError(
            "Invalid API key. Check your OPENAI_API_KEY in the .env file."
        )

    except RateLimitError:
        # Too many requests or out of credits
        raise RuntimeError(
            "Rate limit hit. Either slow down requests or check your OpenAI billing."
        )

    except APIConnectionError:
        # Network issue
        raise ConnectionError(
            "Could not connect to OpenAI. Check your internet connection."
        )

    except Exception as e:
        # Catch-all for unexpected errors
        raise RuntimeError(f"Unexpected error calling LLM: {str(e)}")


# Test it
if __name__ == "__main__":
    try:
        result = call_llm("What is 2 + 2?")
        print("Result:", result)
    except Exception as e:
        print("Error:", e)
