import sqlite3

from src.database.utils.database_path import get_database_route
from src.security.password_hasher import hash_password
from src.utils.error_handler import log_error

def create_client(account_holder_name, client_cedula, client_password, client_email, client_phone_number, client_age):
    try:
        password = hash_password(client_password)

        with sqlite3.connect(get_database_route()) as connection:
            cursor = connection.cursor()
            
            try:
                cursor.execute("INSERT INTO clients (account_holder_name, client_cedula, client_password, client_email, client_phone_number, client_age) VALUES (?, ?, ?, ?, ?, ?)", (account_holder_name, client_cedula, password, client_email, client_phone_number, client_age))
                connection.commit()

                return True
            except sqlite3.Error:
                return False

    except Exception as error:
        log_error(error)