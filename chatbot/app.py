from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if os.getenv("LANGCHAIN_API_KEY"):
    os.environ["LANGCHAIN_TRACING_V2"] = "true"
    os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")


# Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful assistant. Please respond clearly "
            "and accurately to the user's questions."
        ),
        (
            "user",
            "Question: {question}"
        )
    ]
)

## Streamlit framework
st.title("AI Chatbot")
st.caption("Powered by LangChain and Google Gemini")

if not GOOGLE_API_KEY:
    st.error("The app is missing its GOOGLE_API_KEY configuration.")
    st.stop()

input_text = st.text_input(
    "Enter your question here:"
)

 ## googleAI LLM 
llm = ChatGoogleGenerativeAI(model="gemini-3.6-flash", google_api_key=GOOGLE_API_KEY,
                             temperature=0.7, max_output_tokens=1024) 

##output parser 
output_parser = StrOutputParser() 

chain = prompt|llm|output_parser 

if input_text:
    with st.spinner("Generating response..."):
        try:
            response = chain.invoke(
                {
                    "question": input_text
                }
            )
            st.write("### 🤖 Assistant")
            st.write(response)
        except Exception as e:
            st.error(f"Error: {e}")
