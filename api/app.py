from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.llms import Ollama
from langserve import add_routes

import os
import uvicorn
from dotenv import load_dotenv


# Load environment variables
load_dotenv()

os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY", "")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY", "")


# Create FastAPI app
app = FastAPI(
    title="LangChain Google Gemini Chatbot API",
    version="1.0",
    description="API powered by LangChain, Google Gemini and Ollama."
)


# Gemini model
model = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0.7
)


# Ollama model
llm = Ollama(
    model="llama2"
)


# Simple Gemini chatbot route
add_routes(
    app,
    model,
    path="/chat"
)


# Essay prompt
prompt1 = ChatPromptTemplate.from_template(
    "Write me an essay about {topic} with 100 words."
)


# Poem prompt
prompt2 = ChatPromptTemplate.from_template(
    "Write me a poem about {topic} with 100 words."
)


# Output parser
parser = StrOutputParser()


# Essay chain
essay_chain = prompt1 | model | parser

# Poem chain
poem_chain = prompt2 | llm | parser


# Add routes
add_routes(
    app,
    essay_chain,
    path="/essay"
)

add_routes(
    app,
    poem_chain,
    path="/poem"
)


# Run server
if __name__ == "__main__":
    uvicorn.run(
        app,
        host="localhost",
        port=8000
    )