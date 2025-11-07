import wikipedia
from src.assistant.core.skill_base import Skill

class WikipediaSkill(Skill):
    name = "wikipedia"

    def can_handle(self, text: str) -> bool:
        return "wikipedia" in text

    def handle(self, text: str) -> str:
        query = text.replace("wikipedia", "").strip()
        if not query:
            return "Please specify a topic for Wikipedia."
        try:
            result = wikipedia.summary(query, sentences=2)
            return f"According to Wikipedia: {result}"
        except Exception:
            return "Sorry, I couldn't find anything."
