import asyncio
import httpx


class WebFetcher:

    def __init__(self, timeout=20):
        self.timeout = timeout

    async def fetch(self, url: str) -> str:
        headers = {
            "User-Agent": (
                "Mozilla/5.0 "
                "AppleWebKit/537.36 "
                "Chrome/138 Safari/537.36"
            )
        }

        async with httpx.AsyncClient(
            headers=headers,
            timeout=self.timeout,
            follow_redirects=True,
        ) as client:

            response = await client.get(url)
            response.raise_for_status()

            return response.text

    async def fetch_many(self, urls: list[str]) -> list[str]:

        tasks = [self.fetch(url) for url in urls]

        return await asyncio.gather(
            *tasks,
            return_exceptions=True,
        )