from enum import Enum

class HttpStatus(Enum):
    OK = 200
    NOT_FOUND = 404

HYPERLINK_PATTERN = r'https?://[\w.-]+(?:\.[\w.-]+)*(?:[/?#][^\s]*)?'