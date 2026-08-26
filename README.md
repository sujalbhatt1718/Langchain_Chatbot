# LangChain LLM Projects

A collection of small LLM applications built with LangChain. The repository includes Streamlit chatbots, a FastAPI/LangServe API, and a retrieval-augmented generation (RAG) example.

## Included projects

| Folder | Project | Description |
| --- | --- | --- |
| `chatbot/` | Gemini chatbot | Streamlit chat interface powered by Google Gemini. |
| `chatbot/localama.py` | Local chatbot | Streamlit chatbot that runs Llama 2 locally through Ollama. |
| `api/` | LangServe API | FastAPI service exposing Gemini chat, essay, and Ollama poem chains. Includes a Streamlit API client. |
| `groq/` | Groq RAG chatbot | Answers questions from LangSmith documentation using web loading, Hugging Face embeddings, and Chroma. |
| `rag/` | RAG resources | Sample notebook and source documents for RAG experimentation. |

## Tech stack

- Python, LangChain, and LangServe
- Streamlit and FastAPI
- Google Gemini, Groq, and Ollama / Llama 2
- ChromaDB and Hugging Face sentence-transformer embeddings

## Setup

1. Create and activate a virtual environment.

   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

2. Install dependencies.

   ```powershell
   pip install -r requirements.txt
   ```

3. Copy `.env.example` to `.env` and set only the credentials required by the project you will run.

   ```env
   GOOGLE_API_KEY=your_google_api_key
   GROQ_API_KEY=your_groq_api_key
   LANGCHAIN_API_KEY=your_langsmith_api_key
   LANGCHAIN_PROJECT=langchain-chatbot
   ```

   `LANGCHAIN_API_KEY` and `LANGCHAIN_PROJECT` are optional and enable LangSmith tracing. Never commit `.env`.

## Run an application

### Gemini Streamlit chatbot

```powershell
streamlit run chatbot/app.py
```

Requires `GOOGLE_API_KEY`.

### Local Ollama chatbot

Install [Ollama](https://ollama.com/), then download and serve Llama 2:

```powershell
ollama pull llama2
ollama serve
```

In another terminal:

```powershell
streamlit run chatbot/localama.py
```

### FastAPI / LangServe API

Start the service:

```powershell
python api/app.py
```

Then start its Streamlit client in another terminal:

```powershell
streamlit run api/client.py
```

The API listens on `http://localhost:8000`. It needs `GOOGLE_API_KEY` for the Gemini endpoints; the poem endpoint also needs Ollama and Llama 2 running locally.

### Groq RAG chatbot

```powershell
streamlit run groq/app.py
```

Requires `GROQ_API_KEY`. On its first run, it loads LangSmith documentation, creates embeddings with `all-MiniLM-L6-v2`, and stores them in an in-memory Chroma vector store for the session.

## Notes

- The `requirements.txt` file contains dependencies for every example in this repository.
- Model names and prompts are defined directly in the relevant application files and can be changed to suit your account and local setup.
- The local Ollama workflow runs on your machine and does not require a hosted LLM API for responses.

## License

No license has been added yet.
