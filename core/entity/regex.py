import re

HYPERLINK_PATTERN = r'https?://[\w.-]+(?:\.[\w.-]+)*(?:[/?#][^\s]*)?'

def find_hyperlinks(text: str) -> list[str]:
    return re.findall(HYPERLINK_PATTERN, text)
