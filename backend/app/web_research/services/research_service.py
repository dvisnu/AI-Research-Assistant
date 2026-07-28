import asyncio
from app.llm.gemini import get_llm
from app.web_research.search.tavily_search import TavilySearchProvider
from app.web_research.scraping.fetcher import WebFetcher
from app.web_research.extraction.extractor import ContentExtractor

from app.web_research.models.research_response import (
    ResearchResponse,
    Source,
)

from app.web_research.prompts.research_prompt import (
    RESEARCH_PROMPT,
)



class ResearchService:

    def __init__(self):

        self.search = TavilySearchProvider()

        self.fetcher = WebFetcher()

        self.extractor = ContentExtractor()

        self.llm = get_llm()

    async def research(self, query: str) -> ResearchResponse:

        search_results = await self.search.search(query)

        urls = [r.url for r in search_results.results]

        html_pages = await asyncio.gather(
            *[
                self.fetcher.fetch(url)
                for url in urls
            ],
            return_exceptions=True,
        )

        documents = []

        sources = []

        for html, result in zip(html_pages, search_results.results):

            if isinstance(html, Exception):
                continue

            text = self.extractor.extract(html)

            if not text:
                continue

            documents.append(
                f"""
TITLE:
{result.title}

URL:
{result.url}

CONTENT:
{text}
"""
            )

            sources.append(
                Source(
                    title=result.title,
                    url=result.url,
                )
            )

        context = "\n\n".join(documents)

        prompt = RESEARCH_PROMPT.format(
            query=query,
            context=context,
        )

        answer = await self.llm.ainvoke(prompt)

        return ResearchResponse(
            answer=answer.content,
            sources=sources,
        )