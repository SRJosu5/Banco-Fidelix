import sqlite3, time

from src.database.utils.database_path import get_database_route
from src.utils.error_handler import log_error

def get_client_data(client_id):
    try:
        while True:
            with sqlite3.connect(get_database_route()) as connection:
                cursor = connection.cursor()

                cursor.execute("SELECT account_holder_name, client_cedula, client_password, client_email, client_phone_number, client_age FROM clients WHERE ID = ?", (client_id,))
                client_profile_row = cursor.fetchone()

                if client_profile_row:
                    client_data = {
                        "account_holder_name": client_profile_row[0],
                        "client_cedula": client_profile_row[1],
                        "client_password": client_profile_row[2],
                        "client_email": client_profile_row[3],
                        "client_phone_number": client_profile_row[4],
                        "client_age": client_profile_row[5]
                    }
                    return client_data
                else:
                    client_data = {
                        "account_holder_name": "",
                        "client_cedula": "",
                        "client_password": "",
                        "client_email": "",
                        "client_phone_number": "",
                        "client_age": ""
                    }
                    return client_data

    except Exception as error:
        log_error(error)