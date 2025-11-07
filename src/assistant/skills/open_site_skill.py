import webbrowser
from src.assistant.core.skill_base import Skill

class OpenSiteSkill(Skill):
    name = "open_site"
    SITES = {
        "open youtube": "https://www.youtube.com/",
        "open google": "https://www.google.com/",
    }

    def can_handle(self, text: str) -> bool:
        return any(k in text for k in self.SITES)

    def handle(self, text: str) -> str:
        for key, url in self.SITES.items():
            if key in text:
                webbrowser.open(url)
                return f"Opening {key.split()[-1]}..."
        return "Which site should I open?"
