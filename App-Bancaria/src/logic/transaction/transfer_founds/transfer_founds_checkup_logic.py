from src.interface.transaction.transfer_founds.transfer_founds_checkup import transfer_founds_checkup_ui
from src.database.crud.read.client_bank_account_read import get_client_bank_account
from src.database.crud.read.client_addressee_read import get_client_addressee
from src.utils.error_handler import log_error
from src.session import session_data
from tkinter import messagebox

def transfer_founds_checkup_logic(root, entry_deposit, entry_iban_addressee, entry_reason):
    try:
        bank_account = session_data.client_bank_account_data
        client_balance = float(bank_account["client_balance"])
        client_iban = bank_account["client_iban"]
        
        deposit = entry_deposit.get()
        iban_addressee = entry_iban_addressee.get()
        reason = entry_reason.get()

        error_message = None

        try:
            if not deposit and not iban_addressee:
                error_message = "Rellena los campos."
            elif iban_addressee == client_iban:
                error_message = "No puedes hacerte transferencias a ti mismo."
            elif float(deposit) > client_balance:
                error_message = "No tienes suficiente saldo para transferir."
            elif float(deposit) <= 0:
                error_message = "No puedes transferir ese saldo."
            elif not reason:
                reason = "Sin motivo"
            
            if error_message:
                messagebox.showerror("Error", error_message)
            else:
                if get_client_addressee(iban_addressee):
                    transfer_founds_checkup_ui(root, deposit, iban_addressee, reason)
                else:
                    messagebox.showerror("Error", "Ocurrió un problema en la validacion del IBAN.")
        
        except ValueError:
            messagebox.showerror("Error", "Informacion no valida.")

    except Exception as error:
        log_error(error)