# Groq Chatbot Demo

Dockerized Streamlit chatbot with conversation memory. Powered by Groq LLM API.

## Requirements

- [Docker](https://docs.docker.com/get-docker/)
- Groq API key ([get one here](https://console.groq.com))

## Run with Docker
```bash
docker pull msmirnov18/groq-chatbot-demo:latest
docker run -p 8501:8501 -e GROQ_API_KEY=your_key_here msmirnov18/groq-chatbot-demo:latest
```

Open http://localhost:8501

## Run Locally (without Docker)

1. Install [UV](https://docs.astral.sh/uv/): `curl -LsSf https://astral.sh/uv/install.sh | sh`
2. Clone the repo and install dependencies:
```bash
   git clone https://github.com/msmirnov18/groq-chatbot-demo.git
   cd groq-chatbot-demo
   uv sync
```
3. Create `.env` file with your API key:
```
   GROQ_API_KEY=your_key_here
```
4. Run: `uv run streamlit run app.py`

## Tech Stack

- Streamlit
- Groq API (Llama 3.3 70B)
- Docker
- GitHub Actions (CI/CD)