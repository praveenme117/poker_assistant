from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
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

        self.prompt=ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    """ You are a Senior Backend Engineer.
                    Explain concepts clearly.
                    Prefer Java Springboot and node js, typescript examples.
                    Keep answers concise.
                    """,
                ),
                (
                    "human",
                    "{question}",
                ),
            ]
        )

        logger.info("Groq client initialized succesfully")
    

    def chat(self, message:str) -> str:
        logger.info("Received prompt: %s", message)

        messages=self.prompt.invoke(
            {
                "question":message
            }
        )
        logger.info(messages)
        response = self.llm.invoke(messages)
        logger.info("Received response from Groq.")
        return response.content