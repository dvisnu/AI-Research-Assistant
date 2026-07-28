from pydantic import BaseModel


class SearchResult(BaseModel):
    title: str
    url: str
    content: str


class SearchResponse(BaseModel):
    results: list[SearchResult]