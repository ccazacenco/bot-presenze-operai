import os
from pathlib import Path
from dotenv import load_dotenv

# Carica le variabili d'ambiente dal file .env
load_dotenv()

class Config:
    # Usa i nomi delle variabili d'ambiente, non i valori hardcoded!
    TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
    GOOGLE_CREDS_PATH = Path(__file__).parent / "credentials" / "service_account.json"
    DRIVE_ROOT_FOLDER = os.getenv("DRIVE_FOLDER_ID")
