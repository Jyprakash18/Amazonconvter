import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
# Default tag if user hasn't set one
DEFAULT_TAG = "yourdefault-21"
