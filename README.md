# Streamlit Q&A Chatbot with Groq

A simple question-answering chatbot built with Streamlit and Groq. Pick a model, adjust temperature and max tokens from the sidebar, and ask anything.

Built while learning how to wire a LangChain prompt template and Groq LLM into a Streamlit app with configurable model settings.

---

## Setup

```bash
git clone https://github.com/imbhaskarm/streamlit-groq-qna-chatbot.git
cd streamlit-groq-qna-chatbot
python -m venv .venv

# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate

pip install -r requirements.txt
cp .env.example .env
```

Add your Groq API key to `.env`. Get a free key at https://console.groq.com

---

## Run

```bash
streamlit run app.py
```

The API key field in the sidebar pre-fills from `.env` automatically. You can also paste a key directly in the UI.

---

## Features

- Model selector: choose from Llama 3.3 70B, Llama 3.1 8B, Mixtral, or Gemma2
- Temperature and max token sliders
- Groq API key pre-filled from `.env` (can be overridden in the sidebar)
- Clean LCEL chain: `prompt | llm | StrOutputParser()`

---

## Project Structure

```
streamlit-groq-qna-chatbot/
├── app.py             # Streamlit app entry point
├── requirements.txt
├── .env.example
└── .gitignore
```

---

## Tech Stack

| Tool | Purpose |
|---|---|
| Streamlit | Web UI |
| LangChain | Prompt template + chain |
| Groq | LLM inference (fast, free tier available) |

---

## GitHub Topics

`streamlit` `langchain` `groq` `chatbot` `python`
