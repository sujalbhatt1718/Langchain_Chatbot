from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama

import streamlit as st
import os 
from dotenv import load_dotenv

load_dotenv()

## os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY") Not needed as we are using the ollama LLM for local inference.
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")


# Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
           ("system",
            "You are a helpful assistant. Please respond clearly " "and accurately to the user's questions." ), 
            ( "user", "Question: {question}")
    ]
)

#Streamlit framework
st.title("LangChain Google Generative AI")
input_text = st.text_input("Enter your question here:")

# ollama LLM for local inference
llm = Ollama(model="llama2", temperature=0.7, max_output_tokens=1024)

output_parser = StrOutputParser()
chain = prompt | llm | output_parser


if input_text:
    response = chain.invoke({"question": input_text})
    st.write(response)

## To run this type streamlit run localama.py in the terminal and open the link in the browser.
## To run ollama server, type ollama serve in the terminal and make sure you have the model downloaded. 
## You can download the model by typing ollama pull llama2 in the terminal.by typing ollama pull llama2 in the terminal.

## Ollama is a local LLM inference engine that allows you to run LLMs on your local machine without the need for an internet connection. 
## It provides a simple interface for running LLMs and can be used with LangChain for building applications.
## And no cost is involved in using ollama as it runs locally on your machine.