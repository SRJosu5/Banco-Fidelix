import sqlite3

from src.database.utils.database_path import get_database_route
from src.utils.error_handler import log_error

def create_cards(account_holder_name, final_card, random_cvc, expires, client_iban, client_id):
    try:
        try:
            with sqlite3.connect(get_database_route()) as connection:
                cursor = connection.cursor()

                cursor.execute("INSERT INTO bank_cards (account_holder_name, card_number, cvc, expires, client_iban, client_id) VALUES (?, ?, ?, ?, ?, ?)", (account_holder_name, final_card, random_cvc, expires, client_iban, client_id))
                connection.commit()
            
                return True
        except sqlite3.Error as error:
            return False
        
    except Exception as error:
        log_error(error)