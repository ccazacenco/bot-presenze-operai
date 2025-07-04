from telegram import Update
from telegram.ext import CallbackContext, CommandHandler
from utils.excel_generator import create_presence_template
from utils.drive_manager import DriveManager
from utils.time_utils import get_current_month_year
import os

def handle_monthly_report(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    worker = context.bot_data['db'].get_worker(user_id)
    
    month, year = get_current_month_year()
    filename = create_presence_template(
        worker['full_name'],
        month,
        year
    )
    
    drive = DriveManager()
    drive_link = drive.upload_file(filename, worker['drive_folder_id'])
    os.remove(filename)
    
    update.message.reply_text(
        f"✅ Report mensile generato\n"
        f"📅 {month:02d}/{year}\n"
        f"🔗 {drive_link}"
    )

report_handler = CommandHandler('report', handle_monthly_report)
