import unittest
from core.service.hyperlink_service import HyperlinkService

class TestHyperlinkService(unittest.TestCase):
    def test_extract_hyperlinks(self):
        text = "Visit https://example.com and http://test.com"
        links = HyperlinkService.extract_hyperlinks(text)
        self.assertEqual(len(links), 2)
        self.assertEqual(links[0].url, "https://example.com")
        self.assertEqual(links[1].url, "http://test.com")

    def test_no_hyperlinks(self):
        text = "No links here."
        links = HyperlinkService.extract_hyperlinks(text)
        self.assertEqual(len(links), 0)
