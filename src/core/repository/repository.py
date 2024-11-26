from abc import ABC, abstractmethod

class Repository(ABC):
    @abstractmethod
    def save(file_path: str, data: dict) -> None:
        pass

    @abstractmethod
    def load(file_path: str) -> str:
        pass