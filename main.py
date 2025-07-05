
import os
from telegram.ext import ApplicationBuilder
from handlers import setup_handlers

def main():
    application = ApplicationBuilder()\
        .token(os.getenv("TELEGRAM_TOKEN"))\
        .build()
    
    setup_handlers(application)
    
    application.run_polling()

if __name__ == "__main__":
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
