class HyperlinkRepository:
    def __init__(self):
        self.links = []

    def add_link(self, link: str):
        self.links.append(link)

    def get_links(self) -> list[str]:
        return self.links
