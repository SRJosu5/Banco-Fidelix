import sqlite3, time

from src.database.utils.database_path import get_database_route
from src.utils.error_handler import log_error

def get_client_envelopes(client_id):
    try:
        while True:
            with sqlite3.connect(get_database_route()) as connection:
                cursor = connection.cursor()

                cursor.execute("SELECT * FROM client_envelopes WHERE client_id = ?", (client_id,))
                client_envelopes_row = cursor.fetchall()

                return client_envelopes_row

    except Exception as error:
        log_error(error)