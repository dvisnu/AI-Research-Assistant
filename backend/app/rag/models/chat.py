from pydantic import BaseModel


class ChatRequest(BaseModel):
    question: str


class Source(BaseModel):
    filename: str
    page: int | None = None
    chunk_id: int | None = None


class ChatResponse(BaseModel):
    answer: str
    sources: list[Source]
