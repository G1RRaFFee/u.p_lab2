from src.core.service.hyperlink_service import HyperlinkSearchService
from src.core.entity.model import SearchResult

class HyperlinkSearchController:
    def __init__(self, hyperlink_search_service: HyperlinkSearchService):
        self.hyperlink_search_service = hyperlink_search_service

    def search_in_text(self, text: str) -> SearchResult:
        result = self.hyperlink_search_service.search_in_text(text)
        return result

    def search_in_file(self, file_path: str) -> SearchResult:
        result = self.hyperlink_search_service.search_in_file(file_path)
        return result
    
    def search_in_url(self, url: str) -> SearchResult:
        result = self.hyperlink_search_service.search_in_url(url)
        return result