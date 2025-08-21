import os

from src.utils.error_handler import log_error

def get_database_route():
    try:
        database = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', 'database', 'bank.db'))
        return database
    except Exception as error:
        log_error(error)