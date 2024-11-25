import subprocess
import os
import json
import unittest

class TestMain(unittest.TestCase):

    def test_search_in_text(self):
        result = subprocess.run(
            ["python", "main.py", "--input", "Check https://example.com", "--output", "test_result.json"],
            capture_output=True, text=True
        )
        self.assertEqual(result.returncode, 0)
        with open("test_result.json", "r") as file:
            data = json.load(file)
            self.assertIn("https://example.com", data["links"])
        os.remove("test_result.json")

    def test_search_in_file(self):
        with open("test_file.txt", "w") as file:
            file.write("Visit https://example.com")
        
        result = subprocess.run(
            ["python", "main.py", "--file", "test_file.txt", "--output", "test_result.json"],
            capture_output=True, text=True
        )
        self.assertEqual(result.returncode, 0)
        with open("test_result.json", "r") as file:
            data = json.load(file)
            self.assertIn("https://example.com", data["links"])
        
        os.remove("test_file.txt")
        os.remove("test_result.json")

    def test_search_in_url(self):
        url = "https://example.com"
        result = subprocess.run(
            ["python", "main.py", "--url", url, "--output", "test_result.json"],
            capture_output=True, text=True
        )
        self.assertEqual(result.returncode, 0)
        with open("test_result.json", "r") as file:
            data = json.load(file)
            self.assertIn(url, data["links"])
        os.remove("test_result.json")

if __name__ == '__main__':
    unittest.main()
