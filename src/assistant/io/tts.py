import pyttsx3

_engine = None

def _get_engine():
    global _engine
    if _engine is None:
        _engine = pyttsx3.init()
    return _engine

def speak(text: str) -> None:
    """Say text locally; print as fallback."""
    print(f"Assistant: {text}")
    try:
        engine = _get_engine()
        engine.say(text)
        engine.runAndWait()
    except Exception:
        pass
