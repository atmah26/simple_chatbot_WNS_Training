# 🤖 AI Multi-Mode Chatbot

A Streamlit-powered chatbot app with three modes — General Chatbot, Story Generator, and Joke Generator — built with LangChain and Google Gemini.

## Features

- **Chatbot** — General purpose conversational AI with full memory
- **Story Generator** — Generates short creative stories based on your prompts
- **Joke Generator** — Produces puns and one-liners on any topic
- **Mode switching** — Sidebar radio buttons to switch modes; history resets automatically on switch

## Tech Stack

- [Streamlit](https://streamlit.io/) — UI and session management
- [LangChain](https://www.langchain.com/) — LLM abstraction layer
- [Google Gemini](https://ai.google.dev/) — Underlying language model

## Project Structure

```
project/
│
├── app.py          # Main application file
└── README.md       # This file
```

## Setup & Installation

**1. Clone or download the project**

**2. Install dependencies**
```bash
pip install streamlit langchain-google-genai
```

**3. Get a free Gemini API key**

Go to [https://aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey) and create a free key.

**4. Add your API key in `app.py`**
```python
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key="YOUR_API_KEY_HERE"
)
```

**5. Run the app**
```bash
streamlit run app.py
```

## How It Works

### Memory (Conversation History)
The app stores conversation history in `st.session_state` — a Streamlit mechanism that persists data across reruns. On every message, the full history is sent to the AI so it can respond in context.

### Mode Switching
The selected mode is also stored in `st.session_state`. On every rerun, the app compares the currently selected mode to the stored one. If they differ, the history is cleared and the mode is updated.

### System Prompts
Each mode has a system prompt — a `SystemMessage` that tells the AI how to behave. It is injected at the top of the messages list on every API call but is **not** stored in the history, since it is behaviour, not conversation.

```python
system_prompts = {
    "Chatbot": "You are a helpful assistant.",
    "Story Generator": "You are a creative story writer...",
    "Joke Generator": "You are a witty comedian..."
}
```

### Message Flow

```
User types message
        ↓
Append HumanMessage → st.session_state.messages
        ↓
Inject SystemMessage at top → get_messages_with_system()
        ↓
Send full list → LangChain → Gemini
        ↓
Append AIMessage → st.session_state.messages
        ↓
Streamlit displays everything
```
## Key Concepts Learned

- `st.session_state` for persisting data across Streamlit reruns
- LangChain's `HumanMessage`, `AIMessage`, and `SystemMessage`
- How LLM conversation memory works (full history per request)
- System prompts to control AI behaviour
- Token-based billing implications of long conversations
