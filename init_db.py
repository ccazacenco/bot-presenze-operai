import sys
import os

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from utils.db_manager import init_db

if __name__ == "__main__":
    init_db()
