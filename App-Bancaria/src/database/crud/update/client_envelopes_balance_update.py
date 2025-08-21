import sqlite3

from src.database.utils.database_path import get_database_route
from src.utils.error_handler import log_error

def update_client_envelopes_balance(deposit, envelope_name, client_id):
    try:
        try:
            with sqlite3.connect(get_database_route()) as connection:
                cursor = connection.cursor()

                cursor.execute("UPDATE client_envelopes SET client_balance = client_balance + ? WHERE envelope_name = ? AND client_id = ?", (deposit, envelope_name, client_id))
                cursor.execute("UPDATE bank_accounts SET client_balance = client_balance - ? WHERE client_id = ?", (deposit, client_id))
                connection.commit()

                return True
        except sqlite3.Error as error:
            print(error)
            return False

    except Exception as error:
        log_error(error)