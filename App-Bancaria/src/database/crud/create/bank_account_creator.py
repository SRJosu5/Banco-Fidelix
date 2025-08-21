import sqlite3

from src.database.utils.database_path import get_database_route
from src.utils.error_handler import log_error

def create_bank_account(account_holder_name, bank_account_type, client_iban, client_phone_number, client_id):
    try:
        try:
            with sqlite3.connect(get_database_route()) as connection:
                cursor = connection.cursor()

                cursor.execute("INSERT INTO bank_accounts (account_holder_name, client_bank_account_type, client_iban, client_phone_number, client_balance, client_id) VALUES (?, ?, ?, ?, ?, ?)", (account_holder_name, bank_account_type, client_iban, client_phone_number, 0.0, client_id))
                connection.commit()
                
                return True
        except sqlite3.Error:
            return False

    except Exception as error:
        log_error(error)