import re
from typing import List

HYPERLINK_PATTERN = r'https?://[^\s]+'

def find_hyperlinks(text: str) -> List[str]:
    return re.findall(HYPERLINK_PATTERN, text)
