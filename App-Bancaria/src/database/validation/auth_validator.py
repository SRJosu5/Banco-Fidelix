import sqlite3, time

from src.database.utils.database_path import get_database_route
from src.security.password_hasher import hash_password
from src.utils.error_handler import log_error
from src.session import session_data

def validate_login(client_cedula, client_password):
    try:
        from src.service.client_updater import session_service_thread

        inicio = time.time()
        inicio2 = time.time()

        password = hash_password(client_password)

        with sqlite3.connect(get_database_route()) as connection:
            cursor = connection.cursor()

            cursor.execute("SELECT id FROM clients WHERE client_cedula = ? AND client_password = ?", (client_cedula, password))
            client_row = cursor.fetchone()

        if client_row:
            session_data.client_id = client_row[0]
            fin = time.time()
            print(f"Usuario validado en {fin-inicio} ms")
            session_service_thread(client_row[0])
            fin2 = time.time()
            print(f"Informacion cargada en {fin2 - inicio2} ms")
            return True
        else:
            return False

    except sqlite3.DatabaseError as error:
        log_error(error)