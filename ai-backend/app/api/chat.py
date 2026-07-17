from fastapi import APIRouter

from app.models.chat_request import ChatRequest
from app.models.chat_response import ChatResponse
from app.services.llm_service import LLMService

router = APIRouter(
    prefix="/chat",
    tags=["Chat"],
)

llm_service = LLMService()

router.post(
    "",
    response_model=ChatResponse,
)

def chat(request: ChatRequest):
    response = llm_service.chat(request.message)
    return ChatResponse(response=response)