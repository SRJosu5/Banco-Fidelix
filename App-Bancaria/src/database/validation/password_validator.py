import sqlite3, hashlib

from src.database.utils.database_path import get_database_route
from src.security.password_hasher import hash_password
from src.utils.error_handler import log_error

def validate_old_password(old_client_password):
    try:
        password = hash_password(old_client_password)

        with sqlite3.connect(get_database_route()) as connection:
            cursor = connection.cursor()

            cursor.execute("SELECT * FROM clients WHERE client_password = ?", (password,))
            client_row = cursor.fetchone()

            if client_row:
                return True
            else:
                return False
        
    except Exception as error:
        log_error(error)