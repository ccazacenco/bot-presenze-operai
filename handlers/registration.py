from telegram import Update
from telegram.ext import CommandHandler, CallbackContext

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        "Benvenuto! Usa i comandi per registrarti e gestire le tue presenze."
    )

registration_handler = CommandHandler('start', start)
