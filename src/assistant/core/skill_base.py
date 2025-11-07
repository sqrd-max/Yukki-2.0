from abc import ABC, abstractmethod

class Skill(ABC):
    name: str = "base"

    @abstractmethod
    def can_handle(self, text: str) -> bool: ...
    @abstractmethod
    def handle(self, text: str) -> str: ...
