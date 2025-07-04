
import os
from telegram.ext import Updater
from dotenv import load_dotenv
from handlers import setup_handlers
from utils.time_utils import should_be_active

load_dotenv()
from flask import Flask
app = Flask(__name__)

@app.route('/health')
def health_check():
    return "OK", 200

def main():
    updater = Updater(token=os.getenv("TELEGRAM_TOKEN"), use_context=True)
    setup_handlers(updater.dispatcher)

    print("🤖 Bot avviato - In attesa di comandi...")
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
