from src.database.crud.read.client_bank_account_read import get_client_bank_account
from src.interface.bank_account.account.bank_account_ui import bank_account_ui
from src.interface.envelopes.envelopes_ui import envelopes_ui
from src.utils.error_handler import log_error
from src.session import session_data
from tkinter import messagebox

def display_envelopes_warning_logic(root):
    try:
        bank_account = session_data.client_bank_account_data

        client_iban = bank_account["client_iban"]

        if not client_iban:
            messagebox.showerror("Error", "Aun no tienes una cuenta bancaria, crea una primero.")
            bank_account(root)
            return False
        else:
            answer = messagebox.askquestion("Opcion en desarollo", "Estas entrando a una opcion en desarollo y pueden haber fallas criticas. Deseas entrar?")
            if answer == "yes":
                envelopes_ui(root)
            else:
                return False

    except Exception as error:
        log_error(error)