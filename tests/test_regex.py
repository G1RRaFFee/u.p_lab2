import unittest
from core.entity.regex import find_hyperlinks

class TestRegex(unittest.TestCase):
    def test_find_hyperlinks(self):
        test_data = [
            ("Check out https://example.com and visit http://test.com!", ["https://example.com", "http://test.com"]),
            ("No links here", []),
            ("Only one link: https://test.com", ["https://test.com"]),
            ("Multiple links https://link1.com https://link2.com", ["https://link1.com", "https://link2.com"]),
            ("Invalid URL: test.com", []),  # Не должно быть найдено
        ]
        
        for text, expected in test_data:
            with self.subTest(text=text):
                result = find_hyperlinks(text)
                self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
