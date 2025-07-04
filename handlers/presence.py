from telegram import Update
from telegram.ext import CommandHandler, CallbackContext
from utils.time_utils import should_be_active

def register_presence(update: Update, context: CallbackContext):
    if not should_be_active():
        update.message.reply_text("⏸️ Bot disponibile solo 7:00-22:00 Lun-Sab")
        return

    # Logica registrazione presenza
    update.message.reply_text("Presenza registrata!")

# Definisci presence_handler associato al comando /presence
presence_handler = CommandHandler('presence', register_presence)
