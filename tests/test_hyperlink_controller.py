import unittest
from unittest.mock import patch
from infrastructure.controller.hyperlink_controller import HyperlinkController

class TestHyperlinkController(unittest.TestCase):
    @patch("infrastructure.web.web_handler.WebHandler.fetch_html")
    def test_get_links_from_url(self, mock_fetch_html):
        mock_fetch_html.return_value = "Visit https://example.com"
        links = HyperlinkController.get_links_from_url("http://test.com")
        self.assertEqual(len(links), 1)
        self.assertEqual(links[0].url, "https://example.com")

    @patch("infrastructure.file.file_handler.FileHandler.read_file")
    def test_get_links_from_file(self, mock_read_file):
        mock_read_file.return_value = "Visit https://example.com"
        links = HyperlinkController.get_links_from_file("test.txt")
        self.assertEqual(len(links), 1)
        self.assertEqual(links[0].url, "https://example.com")
