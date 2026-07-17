from langchain_ollama import ChatOllama

class LLMService:
    def __init__(self):
        self.llm = ChatOllama(
            model="qwen2.5-coder:7b",
            temperature=0,
        )

    def chat(self, message:str) -> str:
        response = self.llm.invoke(message)
        return response.content