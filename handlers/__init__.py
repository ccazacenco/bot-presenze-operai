from .registration import registration_handler
from .presence import presence_handler
from .reports import report_handler
from .admin import setup_admin_handlers

def setup_handlers(dispatcher):
    dispatcher.add_handler(registration_handler)
    dispatcher.add_handler(presence_handler)
    dispatcher.add_handler(report_handler)
    dispatcher.add_handler(setup_admin_handler)
