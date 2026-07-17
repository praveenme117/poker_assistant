from fastapi import FastAPI
import logging

from app.api.chat import router as chat_router

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
)

app = FastAPI(
    title="AI Backend",
    description="Backend built with FastAPI, LangChain and LangGraph",
    version="1.0.0"
)

app.include_router(chat_router)

@app.get("/")
def health():
    return {
        "status" : "UP",
        "service": "AI Backend"
    }