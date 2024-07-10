# Code Generator with Multi-agent in crewAI

## Installation

Firstly, you need to install [Ollama](https://ollama.com/download)

Then, pulling llama3:8b

```bash
ollama pull llama3
```

## Usage

You need to clone the source code.
First, you need to create `.env` file like `.env.example`

```bash
GENERAL_LLM = "..."
```

Then, you need to install all required libraries in `requirements.txt`

```bash
pip install -r requirements.txt
```

Finally, run the `main.py` file

```bash
python main.py
```