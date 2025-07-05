import os
from pathlib import Path
from dotenv import load_dotenv 

class Config:
    TELEGRAM_TOKEN = os.getenv("7734347521:AAHpCdItWVUwILotW5oWPa1VOG0WGsIyC5M")
    GOOGLE_CREDS_PATH = Path("credentials/service_account.json")
    DRIVE_ROOT_FOLDER = os.getenv("18FK5EcYz5hOm3OZiK0shmx0QTRR0fNxw")
