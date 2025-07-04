from telegram import Update
from telegram.ext import CommandHandler, CallbackContext

def presence(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Qui puoi registrare o vedere le tue presenze.")

presence_handler = CommandHandler('presence', presence)
