from telegram.ext import CommandHandler, MessageHandler, filters
from .admin import admin_command, setup_admin_handlers

def setup_handlers(application):
    # Aggiungi i singoli handler uno per uno
    application.add_handler(CommandHandler("admin", admin_command))
    
    # Oppure se setup_admin_handlers restituisce una lista:
    # for handler in setup_admin_handlers():
    #     application.add_handler(handler)
