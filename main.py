
import os
from telegram.ext import Updater
from telegram.ext import ApplicationBuilder
from dotenv import load_dotenv
from handlers import setup_handlers
from utils.time_utils import should_be_active
def main():
    try:
        application = ApplicationBuilder() \
            .token(os.getenv("TELEGRAM_TOKEN")) \
            .build()
        
        setup_handlers(application)
        print("🤖 Bot avviato correttamente")
        application.run_polling()
    except Exception as e:
        print(f"❌ Errore: {str(e)}")
        raise

if __name__ == '__main__':
    main()
load_dotenv()

def main():
    # Nuova sintassi per v20+
    application = ApplicationBuilder() \
        .token(os.getenv("TELEGRAM_TOKEN")) \
        .build()
    
    setup_handlers(application)
    
    print("🤖 Bot avviato - In attesa di messaggi...")
    application.run_polling()

if __name__ == '__main__':
    main()
