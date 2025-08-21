from src.database.crud.read.client_bank_account_read import get_client_bank_account
from src.database.crud.read.client_phone_number_read import get_client_phone_number
from src.utils.error_handler import log_error
from src.session import session_data
from tkinter import messagebox

def SINPE_checkup_logic(root, entry_deposit, entry_SINPE, entry_reason):
    try:
        from src.interface.transaction.SINPE_movil.SINPE_chekup_ui import SINPE_checkup_ui

        bank_account = session_data.client_bank_account_data
        client_balance = float(bank_account["client_balance"])
        client_phone_number = bank_account["client_phone_number"]
        
        go = 1.1

        deposit = entry_deposit.get()
        SINPE = entry_SINPE.get()
        reason = entry_reason.get()

        error_message = None

        try:
            if not deposit and not SINPE:
                error_message = "Rellena los campos."
            elif str(SINPE) == str(client_phone_number):
                error_message = "No puedes hacerte SINPES a ti mismo."
            elif float(deposit) > client_balance:
                error_message = "No tienes suficiente saldo para transferir."
            elif float(deposit) <= 0:
                error_message = "No puedes transferir ese saldo."
            elif not reason:
                reason = "Sin motivo"

            if error_message:
                messagebox.showerror("Error", error_message)
            else:
                if get_client_phone_number(SINPE):
                    SINPE_checkup_ui(root, deposit, SINPE, reason)
                else:
                    messagebox.showerror("Error", "Ocurrió un problema en la validacion del IBAN.")
                
        except ValueError:
            messagebox.showerror("Error", "Informacion no valida.")

    except Exception as error:
        log_error(error)