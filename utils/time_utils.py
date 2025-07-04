from datetime import datetime
import os
import yaml
from datetime import datetime

def get_current_month_year():
    now = datetime.now()
    return now.month, now.year

def should_be_active():
    """Controlla se il bot deve essere attivo"""
    now = datetime.now()
    config = load_config()
    
    work_days = config["work_days"]  # [0,1,2,3,4,5] per Lun-Sab
    start_hour = config["start_hour"]  # 7
    end_hour = config["end_hour"]  # 22
    
    is_work_day = now.weekday() in work_days
    is_work_time = start_hour <= now.hour < end_hour
    
    return is_work_day and is_work_time

def load_config():
    with open("config.yaml") as f:
        return yaml.safe_load(f)
