from langchain.llms.ollama import Ollama


class LLMs:
    def get_llm(self, model: str = "llama3", base_url: str = "http://localhost:11434"):
        return Ollama(model=model, base_url=base_url)
