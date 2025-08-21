import sqlite3, time

from src.database.utils.database_path import get_database_route
from src.utils.error_handler import log_error

def get_client_bank_account(client_id):
    try:
        while True:
            with sqlite3.connect(get_database_route()) as connection:
                cursor = connection.cursor()

                cursor.execute("SELECT account_holder_name, client_bank_account_type, client_iban, client_balance, client_phone_number FROM bank_accounts WHERE client_id = ?", (client_id,))
                client_bank_account_row = cursor.fetchone()

                if client_bank_account_row:
                    bank_account_data = {
                        "account_holder_name": client_bank_account_row[0],
                        "client_bank_account_type": client_bank_account_row[1],
                        "client_iban": client_bank_account_row[2],
                        "client_balance": client_bank_account_row[3],
                        "client_phone_number": client_bank_account_row[4]
                    }
                    return bank_account_data
                elif client_bank_account_row is None:
                    bank_account_data = {
                        "client_iban": "",
                        "client_bank_account_type": "",
                        "client_balance": ""
                    }
                    return bank_account_data

    except Exception as error:
        log_error(error)