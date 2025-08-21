from src.interface.transaction.SINPE_movil.SINPE_movil_ui import SINPE_movil_ui
from src.database.crud.update.client_balance_update import update_balance_SINPE
from src.utils.error_handler import log_error
from src.session import session_data
from tkinter import messagebox

def SINPE_logic(root, deposit, SINPE, reason):
    try:
        if update_balance_SINPE(int(deposit), SINPE, session_data.client_id):
            messagebox.showinfo("Transferencia exitosa", "Tu SINPE se realizo con exito.")
            SINPE_movil_ui(root)
        else:
            messagebox.showerror("Error de transferencia", "Ocurrio un error mientras se hacia el SINPE.")
            SINPE_movil_ui(root)
            
    except Exception as error:
        log_error(error)