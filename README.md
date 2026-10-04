# LangChain Agents 

A hands-on, step-by-step Python environment for building **LLM-powered agents** with **LangChain** and **LangGraph**, following the setup guide.

## 🚀 About the Project

This project is the foundation of a series on building AI agents. It sets up a clean, isolated Python environment, connects to a Chat LLM (OpenAI by default, swappable for Anthropic or Google), and demonstrates the core LangChain patterns: structured chat messages, synchronous calls, streaming responses, and production-grade error handling.

### Key Features

*   **🔑 Secure API Key Handling**: Environment variables loaded safely from a `.env` file via `python-dotenv`, never hardcoded.
*   **💬 Chat LLM Integration**: `ChatOpenAI` wired up with `SystemMessage`/`HumanMessage` for structured, predictable conversations.
*   **🔄 Swappable LLM Providers**: Same code works with OpenAI, Anthropic (Claude), or Google (Gemini) — just swap the chat model class.
*   **📡 Streaming Responses**: Token-by-token streaming for a responsive, real-time chat experience.
*   **🛡️ Robust Error Handling**: Graceful handling of authentication errors, rate limits, and connection issues.
*   **🧩 LangGraph Ready**: `langgraph` installed and ready for building graph-based, multi-step agent workflows in later steps of the series.

## 🛠️ Technology Stack

*   **Core Framework**: [LangChain](https://www.langchain.com) (`langchain`, `langchain-core`)
*   **Agent Workflows**: [LangGraph](https://langchain-ai.github.io/langgraph/)
*   **LLM Provider**: [OpenAI](https://platform.openai.com) (`gpt-4o-mini`) via `langchain-openai`
*   **Optional Providers**: [Anthropic](https://www.anthropic.com) (`langchain-anthropic`), [Google Gemini](https://ai.google.dev) (`langchain-google-genai`)
*   **Config**: [python-dotenv](https://pypi.org/project/python-dotenv/)
*   **Language**: Python 3.9+

## 🏁 Getting Started

### Prerequisites

*   Python 3.9 or higher
*   An [OpenAI API key](https://platform.openai.com/api-keys) (or an Anthropic/Google key if using a different provider)

### Installation

1.  **Clone the repository**
    ```bash
    git clone https://github.com/Meruem2796/LangChain_agent.git
    cd LangChain_agent
    ```

2.  **Create and activate a virtual environment**
    ```bash
    python -m venv venv

    # Mac/Linux
    source venv/bin/activate

    # Windows
    venv\Scripts\activate
    ```

3.  **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Setup environment variables**

    Create a `.env` file at the project root:
    ```env
    OPENAI_API_KEY=sk-your-actual-key-goes-here

    # Optional, if using an alternate provider
    # ANTHROPIC_API_KEY=your-anthropic-key
    # GOOGLE_API_KEY=your-google-key
    ```
    This file is listed in `.gitignore` and must never be committed.

5.  **Run your first agent call**
    ```bash
    python hello_agent.py
    ```

## 📂 Project Structure

```
langchain-agents-series/
├── .env                      # Your API keys (never commit this)
├── .gitignore                # Ignores .env, venv/, __pycache__/
├── requirements.txt          # Pinned dependencies
├── venv/                     # Virtual environment
├── hello_agent.py            # First LangChain chat LLM call
├── streaming_example.py      # Token-by-token streaming responses
└── error_handling_example.py # Production-grade error handling
```

## 💬 Usage Examples

**Basic chat call** (`hello_agent.py`): sends a system + human message to `gpt-4o-mini` and prints the response along with token usage.

**Streaming** (`streaming_example.py`): streams the model's response chunk by chunk instead of waiting for the full output.

**Error handling** (`error_handling_example.py`): wraps LLM calls with explicit handling for authentication errors, rate limits, and connection failures.

Run any of them with:
```bash
python <script_name>.py
```

## 🔁 Switching LLM Providers

LangChain's unified interface lets you swap providers without changing your application logic:

```python
# Anthropic Claude
from langchain_anthropic import ChatAnthropic
llm = ChatAnthropic(model="claude-3-5-haiku-20241022", temperature=0)

# Google Gemini
from langchain_google_genai import ChatGoogleGenerativeAI
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0)
```

Just install the matching package (`langchain-anthropic` or `langchain-google-genai`) and add the corresponding API key to `.env`.

## ✅ Best Practices Followed

*   Always work inside a virtual environment.
*   Pin dependencies with `pip freeze > requirements.txt`.
*   Never commit `.env` to version control.
*   Use `temperature=0` for predictable agent behavior.
*   Log and monitor token usage to keep costs in check.

## 📝 License

This project is open-sourced software licensed under the [MIT license](https://opensource.org/licenses/MIT).