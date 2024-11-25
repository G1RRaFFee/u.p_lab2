class Hyperlink:
    def __init__(self, url: str):
        self.url = url

    def __repr__(self):
        return f"Hyperlink(url='{self.url}')"
