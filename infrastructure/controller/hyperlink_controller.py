from infrastructure.controller.web.web_handler import WebHandler
from infrastructure.controller.file.file_handler import FileHandler
from core.service.hyperlink_service import HyperlinkService

class HyperlinkController:
    @staticmethod
    def get_links_from_url(url: str):
        html_content = WebHandler.fetch_html(url)
        return HyperlinkService.extract_hyperlinks(html_content)

    @staticmethod
    def get_links_from_file(file_path: str):
        file_content = FileHandler.read_file(file_path)
        return HyperlinkService.extract_hyperlinks(file_content)

    @staticmethod
    def get_links_from_text(text: str):
        return HyperlinkService.extract_hyperlinks(text)
