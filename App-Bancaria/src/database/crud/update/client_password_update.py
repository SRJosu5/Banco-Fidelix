import sqlite3

from src.database.utils.database_path import get_database_route
from src.security.password_hasher import hash_password
from src.utils.error_handler import log_error

def update_password(new_password, client_id):
    try:
        password = hash_password(new_password)
        
        with sqlite3.connect(get_database_route()) as connection:
            cursor = connection.cursor()

            try:
                cursor.execute("UPDATE clients SET password = ? WHERE id = ?", (password, client_id))
                connection.commit()

                return True
            except sqlite3.Error:
                return False

    except Exception as error:
        log_error(error)