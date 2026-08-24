# Local LLM Chatbot

A simple question-answering chatbot built with **Streamlit**, **LangChain**, **Ollama**, and the open-source **Llama 2** large language model. The app runs inference on your own computer through Ollama, so it does not require a paid LLM API for chat responses.

## Features

- Runs an open-source LLM locally with Ollama
- Uses Llama 2 for chatbot responses
- Provides a lightweight browser interface with Streamlit
- Uses LangChain to compose prompts, the model, and output parsing
- Includes an additional `chatbot/app.py` example that connects to Google Gemini (requires an API key)

## Tech stack

| Tool | Purpose |
| --- | --- |
| Python | Application language |
| Streamlit | Web interface |
| LangChain | LLM application framework |
| Ollama | Local LLM runtime/interface |
| Llama 2 | Open-source language model |

## Project structure

```text
LLM/
+-- chatbot/
|   +-- localama.py  # Local Ollama + Llama 2 chatbot
|   +-- app.py       # Google Gemini chatbot example
+-- requirements.txt
+-- README.md
```

## Prerequisites

- Python 3.10 or later
- [Ollama](https://ollama.com/) installed and available on your command line
- The Llama 2 model downloaded locally

## Installation

1. Clone this repository and open the project folder.

2. Create and activate a virtual environment.

   **Windows (PowerShell)**

   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

3. Install Python dependencies.

   ```powershell
   pip install -r requirements.txt
   ```

4. Download the model with Ollama.

   ```powershell
   ollama pull llama2
   ```

## Run the local chatbot

Start the Ollama server in one terminal:

```powershell
ollama serve
```

In another terminal, with the virtual environment activated, start Streamlit:

```powershell
streamlit run chatbot/localama.py
```

Open the local URL shown by Streamlit (usually `http://localhost:8501`). Enter a question and the Llama 2 model will generate a response.

## How it works

1. Streamlit collects the question from the user.
2. LangChain inserts it into a chat prompt.
3. LangChain sends the prompt to Ollama.
4. Ollama runs the local Llama 2 model.
5. The generated response is displayed in the Streamlit interface.

## Testing and observability with LangSmith

This project was tested with **LangSmith** to trace and inspect the LangChain workflow. LangSmith helps monitor the prompt, model call, execution flow, response, and any errors while the chatbot is running.

To enable tracing, add the following values to your local `.env` file:

```env
LANGCHAIN_API_KEY=your_langsmith_api_key
LANGCHAIN_PROJECT=langchain-chatbot
```

Tracing is optional. The chatbot continues to run when these values are not configured.

## Using another Ollama model

To use a different model, first download it, for example:

```powershell
ollama pull mistral
```

Then change this line in `chatbot/localama.py`:

```python
llm = Ollama(model="llama2", temperature=0.7, max_output_tokens=1024)
```

to:

```python
llm = Ollama(model="mistral", temperature=0.7, max_output_tokens=1024)
```

## Gemini example

`chatbot/app.py` is a separate chatbot implementation using Google Gemini through `langchain-google-genai`. It requires a Google API key and is not the local/open-source workflow described above. Store any API key in `.env`; do not hard-code or commit it.

## Deploy to Streamlit Community Cloud

The public deployment uses `chatbot/app.py`, which connects to Google Gemini. The local Ollama application in `chatbot/localama.py` cannot be deployed to Streamlit Community Cloud because it requires an Ollama server and a locally downloaded model.

1. Push the latest changes to GitHub.
2. Go to [Streamlit Community Cloud](https://share.streamlit.io/) and sign in with GitHub.
3. Select the repository `sujalbhatt1718/Langchain_Chatbot`, branch `main`, and set the main file path to `chatbot/app.py`.
4. Open **Advanced settings** and add this secret:

   ```toml
   GOOGLE_API_KEY = "your-new-google-api-key"
   ```

5. Click **Deploy**. Streamlit will create a unique `https://<app-name>.streamlit.app` URL. Add that URL below after the deployment finishes.

### Live demo

Deployment link: [Open the AI Chatbot](https://langchainchatbot-ayeexmjj7uruwlgxgwabhb.streamlit.app/)

## Notes

- Local model speed and quality depend on your computer hardware and the selected model.
- The first response may be slower while Ollama loads the model into memory.
- The current code enables LangChain tracing. Configure the required LangSmith environment values in `.env`, or remove those settings if tracing is not needed.

## License

Add a license file (for example, MIT) before distributing this project publicly.
