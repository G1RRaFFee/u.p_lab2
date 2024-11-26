import re

from src.infrastructure.constants import HYPERLINK_PATTERN

def find_hyperlinks(text: str) -> list[str]:
    return re.findall(HYPERLINK_PATTERN, text)
