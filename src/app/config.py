import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
DEBUG = os.getenv("DEBUG", "False").lower() in ("true", "1")
