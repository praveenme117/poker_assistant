from langchain_groq import ChatGroq
from app.config.settings import settings
import logging

logger = logging.getLogger(__name__)

class LLMService:
    def __init__(self):
        logger.info("Initializing Groq client...")
        self.llm = ChatGroq(
            model=settings.GROQ_MODEL,
            api_key=settings.GROQ_API_KEY,
            temperature=0,
        )

        logger.info("Groq client initialized succesfully")

    def chat(self, message:str) -> str:
        logger.info("Received prompt: %s", message)
        response = self.llm.invoke(message)
        logger.info("Received response from Groq.")
        return response.content