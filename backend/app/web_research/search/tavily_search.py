from tavily import AsyncTavilyClient

from app.config import TAVILY_API_KEY

from .base import BaseSearchProvider
from .schemas import SearchResult, SearchResponse


class TavilySearchProvider(BaseSearchProvider):

    def __init__(self):
        self.client = AsyncTavilyClient(api_key=TAVILY_API_KEY)

    async def search(self, query: str) -> SearchResponse:

        response = await self.client.search(
            query=query,
            max_results=5,
            search_depth="advanced",
        )

        results = [
            SearchResult(
                title=item["title"],
                url=item["url"],
                content=item["content"],
            )
            for item in response["results"]
        ]

        return SearchResponse(results=results)