import sqlite3, time

from src.database.utils.database_path import get_database_route
from src.utils.error_handler import log_error

def get_client_card_data(client_id):
    try:
        while True:
            with sqlite3.connect(get_database_route()) as connection:
                cursor = connection.cursor()

                cursor.execute("SELECT account_holder_name, card_number, cvc, expires, client_iban FROM bank_cards WHERE client_id = ?", (client_id,))
                client_card_data = cursor.fetchone()

                if client_card_data:
                    card_data = {
                        "account_holder_name": client_card_data[0],
                        "card_number": client_card_data[1],
                        "cvc": client_card_data[2],
                        "expires": client_card_data[3],
                        "client_iban": client_card_data[4]
                    }
                    return card_data
                elif client_card_data is None:
                    card_data = {
                        "account_holder_name": "",
                        "card_number": "",
                        "cvc": "",
                        "expires": "",
                        "client_iban": ""
                    }
                    return card_data

    except Exception as error:
        log_error(error)