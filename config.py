import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")

def validate_config() -> None:
    if not GOOGLE_API_KEY:
        return RuntimeError("Missing GOOGLE_API_KEY")