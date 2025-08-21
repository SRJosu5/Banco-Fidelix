import sqlite3

from src.database.utils.database_path import get_database_route
from src.utils.error_handler import log_error

def create_envelopes(name_envelope, client_iban, funds, client_id):
    try:
        try:
            with sqlite3.connect(get_database_route()) as connection:
                cursor = connection.cursor()

                cursor.execute("INSERT INTO client_envelopes (envelope_name, client_iban, client_balance, client_id) VALUES (?, ?, ?, ?)", (name_envelope, client_iban, funds, client_id))
                connection.commit()
                
                return True
        except sqlite3.Error as error:
            print(error)
            return False

    except Exception as error:
        log_error(error)