from typing import List

class SearchResult:
    def __init__(self, source: str, links: List[str]):
        self.source = source
        self.links = links

    def to_dict(self) -> dict:
        return {
            "source": self.source,
            "links": self.links,
        }