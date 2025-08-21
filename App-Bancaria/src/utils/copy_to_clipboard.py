from src.database.crud.read.client_bank_account_read import get_client_bank_account
from src.database.crud.read.client_card_data_read import get_client_card_data
from src.utils.error_handler import log_error
from src.session import session_data
from tkinter import messagebox

def copy_iban_to_clipboard(root):
    try:
        bank_account = session_data.client_bank_account_data
        
        client_iban = bank_account["client_iban"]

        root.clipboard_clear()
        root.clipboard_append(client_iban)
        root.update()

        messagebox.showinfo("Copiado", "El numero IBAN se copio correctamente.")

    except Exception as error:
        log_error(error)

def copy_card_to_clipboard(root):
    try:
        client_card_data = session_data.client_card_data
        
        client_card = client_card_data["card"]
        client_cvc = client_card_data["cvc"]
        client_expires = client_card_data["expires"]

        root.clipboard_clear()
        root.clipboard_append(f"{client_card} {client_cvc} {client_expires}")
        root.update()

        messagebox.showinfo("Copiado", "Los datos de la tarjeta se copiaron correctamente.")

    except Exception as error:
        log_error(error)