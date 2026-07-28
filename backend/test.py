import asyncio

from app.web_research.services.research_service import (
    ResearchService,
)


async def main():

    service = ResearchService()

    result = await service.research(
        "Latest advancements in Retrieval Augmented Generation"
    )

    print("\nANSWER\n")
    print(result.answer)

    print("\nSOURCES\n")

    for source in result.sources:
        print(source.title)
        print(source.url)
        print()


asyncio.run(main())