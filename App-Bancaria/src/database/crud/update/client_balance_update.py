import sqlite3

from src.database.utils.database_path import get_database_route
from src.utils.error_handler import log_error

def update_balance(deposit, iban_addressee, client_id):
    try:
        try:
            with sqlite3.connect(get_database_route()) as connection:
                cursor = connection.cursor()

                cursor.execute("UPDATE bank_accounts SET client_balance = client_balance + ? WHERE client_iban = ?", (deposit, iban_addressee))
                cursor.execute("UPDATE bank_accounts SET client_balance = client_balance - ? WHERE client_id = ?", (deposit, client_id))
                connection.commit()

                return True
        except sqlite3.Error:
            return False

    except Exception as error:
        log_error(error)

def update_balance_SINPE(deposit, SINPE, client_id):
    try:
        try:
            with sqlite3.connect(get_database_route()) as connection:
                cursor = connection.cursor()

                cursor.execute("UPDATE bank_accounts SET client_balance = client_balance + ? WHERE client_phone_number = ?", (deposit, SINPE))
                cursor.execute("UPDATE bank_accounts SET client_balance = client_balance - ? WHERE client_id = ?", (deposit, client_id))
                connection.commit()

                return True
        except sqlite3.Error:
            return False

    except Exception as error:
        log_error(error)