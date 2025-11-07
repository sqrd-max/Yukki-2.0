import pyjokes
from src.assistant.core.skill_base import Skill

class JokesSkill(Skill):
    name = "joke"

    def can_handle(self, text: str) -> bool:
        return "joke" in text

    def handle(self, text: str) -> str:
        return pyjokes.get_joke()
