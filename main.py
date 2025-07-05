import os
from telegram.ext import ApplicationBuilder
from dotenv import load_dotenv
from handlers import setup_handlers


def main():
    try:
        application = ApplicationBuilder() \
            .token(os.getenv("TELEGRAM_TOKEN")) \
            .build()
        setup_handlers(application)
        print("Bot avviato correttamente")
        application.run_polling()
    except Exception as e:
        print(f"Error: {str(e)}")
        raise


if __name__ == "__main__":
    load_dotenv()
    main()
