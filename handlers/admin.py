from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext, CommandHandler, CallbackQueryHandler
from config import Config
import logging

# Setup logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

def setup_admin_handlers(dispatcher):
    """Registra tutti gli handler per i comandi admin"""
    dispatcher.add_handler(CommandHandler("admin", admin_panel))
    dispatcher.add_handler(CallbackQueryHandler(admin_button_handler, pattern='^admin_'))

def admin_panel(update: Update, context: CallbackContext):
    """Mostra il pannello admin"""
    if not is_admin(update.effective_user.id):
        update.message.reply_text("⛔ Accesso negato")
        return

    keyboard = [
        [InlineKeyboardButton("📊 Statistiche", callback_data='admin_stats')],
        [InlineKeyboardButton("🔧 Backup DB", callback_data='admin_backup')],
        [InlineKeyboardButton("📩 Notifica a tutti", callback_data='admin_broadcast')],
        [InlineKeyboardButton("👥 Gestisci Operai", callback_data='admin_workers')]
    ]
    
    update.message.reply_text(
        "🛠️ *Pannello di Amministrazione*",
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode='Markdown'
    )

def admin_button_handler(update: Update, context: CallbackContext):
    """Gestisce le azioni dal pannello admin"""
    query = update.callback_query
    query.answer()
    
    if not is_admin(query.from_user.id):
        query.edit_message_text("⛔ Accesso negato")
        return

    action = query.data.split('_')[1]
    
    if action == 'stats':
        show_stats(query)
    elif action == 'backup':
        create_backup(query)
    elif action == 'broadcast':
        start_broadcast(query)
    elif action == 'workers':
        manage_workers(query)

def is_admin(user_id: int) -> bool:
    """Verifica se l'utente è admin"""
    return str(user_id) == Config.ADMIN_CHAT_ID

def show_stats(query):
    """Mostra statistiche globali"""
    # Esempio: recupera dati dal DB
    stats = {
        'total_workers': 25,
        'active_workers': 18,
        'presences_this_month': 423
    }
    
    query.edit_message_text(
        f"📊 *Statistiche Globali*\n\n"
        f"• Operai totali: {stats['total_workers']}\n"
        f"• Operai attivi: {stats['active_workers']}\n"
        f"• Presenze questo mese: {stats['presences_this_month']}",
        parse_mode='Markdown'
    )

def create_backup(query):
    """Crea e invia un backup del DB"""
    from utils.db_manager import backup_db
    backup_file = backup_db()
    
    if backup_file:
        with open(backup_file, 'rb') as f:
            query.bot.send_document(
                chat_id=query.message.chat_id,
                document=f,
                caption="📦 Backup del database"
            )
        query.edit_message_text("✅ Backup completato")
    else:
        query.edit_message_text("❌ Errore durante il backup")

def start_broadcast(query):
    """Avvia la procedura di broadcast"""
    query.edit_message_text(
        "📢 Inviami il messaggio da inviare a tutti gli operai\n"
        "Usa /cancel per annullare",
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("❌ Annulla", callback_data='admin_cancel')]])
    )
    # Imposta lo stato per il prossimo messaggio
    context.user_data['awaiting_broadcast'] = True

def manage_workers(query):
    """Mostra la lista degli operai"""
    # Esempio: recupera operai dal DB
    workers = [
        {'id': 123, 'name': "Mario Rossi", 'status': "active"},
        {'id': 456, 'name': "Luigi Bianchi", 'status': "inactive"}
    ]
    
    buttons = [
        [InlineKeyboardButton(f"{w['name']} ({w['status']})", callback_data=f'admin_worker_{w["id"]}')]
        for w in workers
    ]
    buttons.append([InlineKeyboardButton("🔙 Indietro", callback_data='admin_back')])
    
    query.edit_message_text(
        "👥 *Lista Operai*",
        reply_markup=InlineKeyboardMarkup(buttons),
        parse_mode='Markdown'
    )

# Aggiungi questo in handlers/__init__.py
# from handlers.admin import setup_admin_handlers
# setup_admin_handlers(dp)
