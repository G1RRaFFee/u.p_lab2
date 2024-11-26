from json import dump

from src.core.repository.repository import Repository

class JsonFileRepository(Repository):
    def load(self, file_path: str) -> str:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()

    def save(self, file_path: str, data: dict) -> None:
        with open(file_path, 'w', encoding='utf-8') as file:
            dump(data, file, indent=4, ensure_ascii=False)
