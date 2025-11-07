import datetime
import sys

from src.assistant.io.tts import speak
from src.assistant.core.dispatcher import IntentDispatcher
from src.assistant.skills.wiki_skill import WikipediaSkill
from src.assistant.skills.open_site_skill import OpenSiteSkill
from src.assistant.skills.time_skill import TimeSkill
from src.assistant.skills.jokes_skill import JokesSkill

from src.assistant.io.asr_sr import take_command, list_microphones

def wish_user() -> None:
    """Greet user based on current hour."""
    hour = int(datetime.datetime.now().hour)
    if hour < 12:
        speak("Good Morning!")
    elif hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am your voice assistant. How can I help you today?")

def run_assistant(lang: str = "en-US") -> None:
    dispatcher = IntentDispatcher([
        WikipediaSkill(),
        OpenSiteSkill(),
        TimeSkill(),
        JokesSkill(),
    ])
    wish_user()
    while True:
        query = take_command(lang=lang)
        if any(w in query for w in ("exit", "bye")):
            speak("Goodbye! Have a nice day!")
            break
        reply = dispatcher.dispatch(query)
        speak(reply)

if __name__ == "__main__":
    # helper: python -m src.assistant.cli --list-mics
    if "--list-mics" in sys.argv:
        list_microphones()
        sys.exit(0)


    run_assistant(lang="en-US")

