from src.database.crud.read.client_bank_account_read import get_client_bank_account
from src.interface.bank_account.account.bank_statement_ui import bank_statement_ui
from src.interface.bank_account.account.bank_account_ui import bank_account_ui
from src.utils.error_handler import log_error
from src.session import session_data 
from tkinter import messagebox

def display_account_warning_logic(root):
    try:
        client_bank_account_data = session_data.client_bank_account_data

        client_iban = client_bank_account_data["client_iban"]

        if not client_iban:
            messagebox.showerror("Error", "Aun no tienes una cuenta bancaria, crea una primero.")
            bank_account_ui(root)
            return False
        else:
            bank_statement_ui(root)

    except Exception as error:
        log_error(error)