import os
import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

# ⚠️ Updated from deprecated os.environ assignment that crashes with None → safe conditional set (latest as of 2025)
langchain_key = os.getenv("LANGCHAIN_API_KEY", "")
if langchain_key:
    os.environ["LANGCHAIN_API_KEY"] = langchain_key
    os.environ["LANGCHAIN_TRACING_V2"] = "true"
    os.environ["LANGCHAIN_PROJECT"] = "Q&A Chatbot with Groq"

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Please respond to the user queries."),
    ("user", "Question: {question}")
])


def generate_response(question, api_key, model_name, temperature, max_tokens):
    llm = ChatGroq(
        model=model_name,
        temperature=temperature,
        max_tokens=max_tokens,
        groq_api_key=api_key
    )
    chain = prompt | llm | StrOutputParser()
    return chain.invoke({"question": question})


st.title("Q&A Chatbot with Groq")
st.sidebar.title("Settings")

api_key = st.sidebar.text_input(
    "Groq API Key",
    type="password",
    value=os.getenv("GROQ_API_KEY", "")
)

model_name = st.sidebar.selectbox(
    "Select Model",
    [
        "llama-3.3-70b-versatile",
        "llama-3.1-8b-instant",
        "mixtral-8x7b-32768",
        "gemma2-9b-it"
    ]
)

temperature = st.sidebar.slider("Temperature", 0.0, 1.0, 0.7)
max_tokens = st.sidebar.slider("Max Tokens", 50, 300, 150)

st.write("Ask any question below:")
user_input = st.text_input("You:")

if user_input:
    if not api_key:
        st.warning("Please enter your Groq API key in the sidebar.")
    else:
        response = generate_response(user_input, api_key, model_name, temperature, max_tokens)
        st.write(response)
