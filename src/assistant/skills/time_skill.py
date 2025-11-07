import datetime
from src.assistant.core.skill_base import Skill

class TimeSkill(Skill):
    name = "time"

    def can_handle(self, text: str) -> bool:
        return "time" in text

    def handle(self, text: str) -> str:
        str_time = datetime.datetime.now().strftime("%H:%M:%S")
        return f"The current time is {str_time}"
