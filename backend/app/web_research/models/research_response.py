from pydantic import BaseModel


class Source(BaseModel):
    title: str
    url: str


class ResearchResponse(BaseModel):
    answer: str
    sources: list[Source]