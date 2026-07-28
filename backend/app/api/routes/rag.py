from fastapi import APIRouter

from app.rag.models.chat import ChatRequest, ChatResponse
from app.rag.chains.rag_chain import ask_question


router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)


@router.post("/", response_model=ChatResponse)
async def chat(request: ChatRequest):
    result = ask_question(request.question)
    return result
