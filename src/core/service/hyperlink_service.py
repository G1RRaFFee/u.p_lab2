from requests import get
from requests.exceptions import RequestException

from core.entity.regex import find_hyperlinks
from core.entity.model import SearchResult
from core.repository.repository import Repository
from infrastructure.constants import HttpStatus

class HyperlinkSearchService:
    def __init__(self, file_repository: Repository):
        self.file_repository = file_repository

    def search_in_text(self, text: str, source: str = "Input Text") -> SearchResult:
        links = find_hyperlinks(text)
        return SearchResult(source=source, links=links)

    def search_in_file(self, file_path: str) -> SearchResult:
        content = self.file_repository.load(file_path)
        links = find_hyperlinks(content)
        return SearchResult(source=file_path, links=links)
    
    def search_in_url(self, url: str) -> SearchResult:
        try:
            response = get(url)
            if response.status_code == HttpStatus.OK.value:
                links = find_hyperlinks(response.text)
                return SearchResult(source=url, links=links)
            else:
                print(f"Error: Unable to fetch URL {url}, Status Code: {response.status_code}")
                return SearchResult(source=url, links=[])
        except RequestException as e:
            print(f"Error: {e}")
            return SearchResult(source=url, links=[])
        
    def save_results(self, result: SearchResult, output_file: str):
        self.file_repository.save(output_file, result.to_dict())
