from fastapi import APIRouter
import logging

from app.models.chat_request import ChatRequest
from app.models.chat_response import ChatResponse
from app.services.llm_service import LLMService

logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/chat",
    tags=["Chat"],
)

llm_service = LLMService()

@router.post(
    "",
    response_model=ChatResponse,
)

def chat(request: ChatRequest):
    logger.info("POST /chat called")
    response = llm_service.chat(request.message)
    logger.info("Returning response to client")
    return ChatResponse(response=response)