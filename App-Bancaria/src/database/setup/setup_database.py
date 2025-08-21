import sqlite3

from src.database.utils.database_path import get_database_route
from src.utils.error_handler import log_error

def create_database():
    try:
        with sqlite3.connect(get_database_route()) as connection:
            cursor = connection.cursor()

            cursor.execute("""
            CREATE TABLE IF NOT EXISTS clients (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                account_holder_name TEXT NOT NULL,
                client_cedula TEXT UNIQUE NOT NULL,
                client_password TEXT NOT NULL,
                client_email TEXT NOT NULL,
                client_phone_number TEXT NOT NULL,
                client_age NUMERIC NOT NULL)
                """)
            
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS bank_accounts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                account_holder_name TEXT NOT NULL,
                client_bank_account_type TEXT NOT NULL,
                client_iban TEXT UNIQUE NOT NULL,
                client_phone_number UNIQUE NOT NULL,
                client_balance REAL DEFAULT 0.0,
                client_id INTEGER,
                FOREIGN KEY (client_id) REFERENCES clients(id))
                """)
            
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                transaction_type TEXT NOT NULL,
                amount REAL NOT NULL,
                date_time TEXT NOT NULL,
                description TEXT NOT NULL,
                client_id INTEGER,
                FOREIGN KEY (client_id) REFERENCES bank_accounts(id))
                """)
            
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS bank_cards (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                account_holder_name TEXT NOT NULL,
                card_number TEXT UNIQUE NOT NULL,
                cvc TEXT NOT NULL,
                expires TEXT NOT NULL,
                client_iban TEXT NOT NULL,
                client_id INTEGER UNIQUE,
                FOREIGN KEY (client_id) REFERENCES clients(id))
                """)
            
            cursor.execute("""   
            CREATE TABLE IF NOT EXISTS client_envelopes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                envelope_name TEXT NOT NULL,
                client_iban TEXT NOT NULL,
                client_balance REAL DEFAULT 0.0,
                client_id INTEGER,
                FOREIGN KEY (client_id) REFERENCES clients(id))
            """)
            
            connection.commit()

    except Exception as error:
        log_error(error)