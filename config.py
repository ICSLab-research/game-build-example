import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv(".env"))


class Config:
    DEFAULT_LLM = os.environ.get("DEFAULT_LLM", "llama3")
    CODER_LLM = os.environ.get("CODER_LLM", "deepseek-coder")
