import trafilatura


class ContentExtractor:

    def extract(self, html: str) -> str:

        text = trafilatura.extract(
            html,
            include_comments=False,
            include_tables=True,
        )

        return text or ""