# utils/config.py
import os

from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

RAW_DATA_PATH = os.getenv("RAW_DATA_PATH")
TRANSFORMED_DATA_PATH = os.getenv("TRANSFORMED_DATA_PATH")
