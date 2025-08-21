from src.interface.transaction.transfer_founds.transfer_funds_ui import transfer_funds_ui
from src.database.crud.update.client_balance_update import update_balance
from src.utils.error_handler import log_error
from src.session import session_data
from tkinter import messagebox

def transfer_founds_logic(root, deposit, iban_addressee, reason):
    try:
        if update_balance(int(deposit), iban_addressee, session_data.client_id):
            messagebox.showinfo("Transferencia exitosa", "Tu transferencia se realizo con exito.")
            transfer_funds_ui(root)
        else:
            messagebox.showerror("Error de transferencia", "Ocurrio un error mientras se transferia el dinero.")
            transfer_funds_ui(root)
            
    except Exception as error:
        log_error(error)