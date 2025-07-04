
import os
from pathlib import Path

class Config:
    TELEGRAM_TOKEN = os.getenv("7734347521:AAHpCdItWVUwILotW5oWPa1VOG0WGsIyC5M")
    GOOGLE_CREDS_PATH = Path("credentials/service_account.json")
    DRIVE_ROOT_FOLDER = os.getenv("DRIVE_ROOT_FOLDER")
