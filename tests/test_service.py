import unittest
from unittest.mock import MagicMock
from core.service.hyperlink_service import HyperlinkSearchService
from core.entity.model import SearchResult
from infrastructure.repository.file_repository import FileRepository

class TestHyperlinkSearchService(unittest.TestCase):
    
    def setUp(self):
        self.mock_file_repo = MagicMock(FileRepository)
        self.service = HyperlinkSearchService(self.mock_file_repo)
    
    def test_search_in_text(self):
        text = "Visit https://example.com for more info."
        expected_links = ["https://example.com"]
        result = self.service.search_in_text(text)
        
        self.assertEqual(result.source, "Input Text")
        self.assertEqual(result.links, expected_links)
    
    def test_search_in_file(self):
        file_content = "Check out https://example.com and http://test.com"
        self.mock_file_repo.read_file.return_value = file_content
        
        file_path = "test_file.txt"
        expected_links = ["https://example.com", "http://test.com"]
        result = self.service.search_in_file(file_path)
        
        self.assertEqual(result.source, file_path)
        self.assertEqual(result.links, expected_links)
    
    def test_search_in_url_success(self):
        # Мокируем запрос
        url = "https://example.com"
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = 'Visit https://example.com for details.'
        
        # Подменяем requests.get для возврата mock_response
        with unittest.mock.patch('requests.get', return_value=mock_response):
            result = self.service.search_in_url(url)
        
        self.assertEqual(result.source, url)
        self.assertEqual(result.links, ["https://example.com"])
    
    def test_search_in_url_failure(self):
        # Мокируем неудачный запрос
        url = "https://nonexistent-url.com"
        mock_response = MagicMock()
        mock_response.status_code = 404
        
        with unittest.mock.patch('requests.get', return_value=mock_response):
            result = self.service.search_in_url(url)
        
        self.assertEqual(result.source, url)
        self.assertEqual(result.links, [])
    
    def test_save_results(self):
        result = SearchResult(source="Input Text", links=["https://example.com"])
        output_file = "output.json"
        
        # Мокируем сохранение файла
        self.mock_file_repo.save_to_json(output_file, result.to_dict())
        
        self.service.save_results(result, output_file)
        
        self.mock_file_repo.save_to_json.assert_called_once_with(output_file, result.to_dict())

if __name__ == '__main__':
    unittest.main()
