from src.interface.bank_account.account.bank_account_ui import bank_account_ui
from src.interface.bank_account.card.manager_card_ui import manager_card_ui
from src.utils.error_handler import log_error
from src.session import session_data 
from tkinter import messagebox

def display_card_warning_logic(root):
    try:
        bank_account = session_data.client_bank_account_data

        client_iban = bank_account["client_iban"]

        if not client_iban:
            messagebox.showerror("Error", "Aun no tienes una cuenta bancaria, crea una primero.")
            bank_account_ui(root)
            return False
        else:
            manager_card_ui(root)

    except Exception as error:
        log_error(error)