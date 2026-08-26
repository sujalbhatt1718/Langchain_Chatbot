import streamlit as st
import os
import time

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_community.document_loaders import WebBaseLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain_classic.chains import create_retrieval_chain
from langchain_community.vectorstores import Chroma

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")

if not groq_api_key:
    st.error("GROQ_API_KEY is not set in your .env file.")
    st.stop()

if "vectors" not in st.session_state:
    st.session_state.embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    st.session_state.loader = WebBaseLoader(
        "https://docs.smith.langchain.com/"
    )

    st.session_state.docs = st.session_state.loader.load()

    st.session_state.text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    st.session_state.final_documents = (
        st.session_state.text_splitter.split_documents(
            st.session_state.docs[:50]
        )
    )

    st.session_state.vectors = Chroma.from_documents(
        documents=st.session_state.final_documents,
        embedding=st.session_state.embeddings
    )


st.title("ChatGroq RAG Chatbot")
llm = ChatGroq(
    groq_api_key=groq_api_key,
    model="openai/gpt-oss-120b",
    temperature=0
)

prompt = ChatPromptTemplate.from_template(
    """
    Answer the question based only on the provided context.

    If the answer is not available in the context,
    say that you don't know.

    <context>
    {context}
    </context>

    Question:
    {input}

    Answer:
    """
)

document_chain = create_stuff_documents_chain(
    llm,
    prompt
)

retriever = st.session_state.vectors.as_retriever(
    search_kwargs={"k": 4}
)

retrieval_chain = create_retrieval_chain(
    retriever,
    document_chain
)

user_prompt = st.text_input("Enter your question:")

if user_prompt:
    start = time.process_time()

    response = retrieval_chain.invoke(
        {"input": user_prompt}
    )

    response_time = time.process_time() - start

    st.write("### Answer")
    st.write(response["answer"])

    st.write(f"Response time: {response_time:.2f} seconds")

    with st.expander("Document Similarity Search"):
        for i, doc in enumerate(response["context"]):
            st.write(f"**Document {i + 1}**")
            st.write(doc.page_content)
            st.write("---")