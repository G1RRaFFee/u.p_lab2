import re
from core.entity.hyperlink import Hyperlink

class HyperlinkService:
    HYPERLINK_PATTERN = re.compile(
        r"https?://(?:www\.)?[\w-]+(?:\.[\w-]+)+[/\w\-._~:/?#[\]@!$&'()*+,;=]*"
    )

    @staticmethod
    def extract_hyperlinks(text: str) -> list[Hyperlink]:
        matches = HyperlinkService.HYPERLINK_PATTERN.findall(text)
        return [Hyperlink(url) for url in matches]
