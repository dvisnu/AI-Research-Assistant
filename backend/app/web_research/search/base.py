from abc import ABC, abstractmethod

from .schemas import SearchResponse


class BaseSearchProvider(ABC):

    @abstractmethod
    async def search(self, query: str) -> SearchResponse:
        pass