from typing import List
from src.assistant.core.skill_base import Skill

class IntentDispatcher:
    """Route text to first skill that can handle it."""
    def __init__(self, skills: List[Skill]) -> None:
        self.skills = skills

    def dispatch(self, text: str) -> str:
        if not text.strip():
            return "Sorry, I didn't hear anything."
        for s in self.skills:
            if s.can_handle(text):
                return s.handle(text)
        return "Sorry, I didn't understand that. Try again."
