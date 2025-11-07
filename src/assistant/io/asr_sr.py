import os
import speech_recognition as sr


def list_microphones() -> None:
    """Print available microphones with their indices."""
    for i, name in enumerate(sr.Microphone.list_microphone_names()):
        print(f"[{i}] {name}")


def take_command(
        lang: str = "en-US",
        device_index: int | None = None,
        timeout: float = 15.0,
        phrase_time_limit: float | None = 10.0,
        ambient_duration: float = 1.0,
) -> str:
    """
    Listen for a voice command via microphone and return recognized text.

    - device_index: pass specific mic index (use list_microphones() to find)
    - timeout: max seconds to wait for speech start (None = wait forever)
    - phrase_time_limit: max seconds of phrase length (None = unlimited)
    - ambient_duration: seconds to calibrate for ambient noise
    """
    # Allow override via env var (e.g. ASSISTANT_MIC_INDEX=1)
    if device_index is None:
        env_idx = os.getenv("ASSISTANT_MIC_INDEX")
        if env_idx is not None and env_idx.isdigit():
            device_index = int(env_idx)

    recognizer = sr.Recognizer()
    # Make the recognizer more tolerant to noise
    recognizer.dynamic_energy_threshold = True
    recognizer.pause_threshold = 0.8  # gap between words considered end of phrase

    try:
        with sr.Microphone(device_index=device_index) as source:
            print(f"Using microphone: {getattr(source, 'device_index', 'default')}")
            # calibrate to ambient noise
            recognizer.adjust_for_ambient_noise(source, duration=ambient_duration)
            print("Listening...")
            audio = recognizer.listen(
                source,
                timeout=timeout,
                phrase_time_limit=phrase_time_limit,
            )
    except sr.WaitTimeoutError:
        print("No speech detected (timeout).")
        return ""
    except OSError as e:
        # e.g., no default input device / bad index
        print(f"Microphone error: {e}")
        return ""

    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio, language=lang)
        print(f"You said: {text}\n")
        return text.lower()
    except sr.UnknownValueError:
        print("Sorry, I didn’t catch that.")
        return ""
    except sr.RequestError:
        print("Speech recognition service is unavailable.")
        return ""
