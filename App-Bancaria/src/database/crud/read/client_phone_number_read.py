import sqlite3

from src.database.utils.database_path import get_database_route
from src.utils.error_handler import log_error
from tkinter import messagebox

def get_client_phone_number(client_phone_number):
    try:
        with sqlite3.connect(get_database_route()) as connection:
            cursor = connection.cursor()

            cursor.execute("SELECT account_holder_name, client_balance FROM bank_accounts WHERE client_phone_number = ?", (client_phone_number,))
            client_transfer_row = cursor.fetchone()

            if client_transfer_row:
                transfer_data = {"account_holder_name": client_transfer_row[0], 
                                "client_balance": client_transfer_row[1],
                                }
                return transfer_data
            else:
                return False

    except Exception as error:
        log_error(error)