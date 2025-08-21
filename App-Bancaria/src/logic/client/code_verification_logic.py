from src.database.crud.update.client_password_update import update_password
from src.database.validation import auth_validator
from src.utils.error_handler import log_error
from tkinter import messagebox

def code_verification(root, entry_code, new_password):
    try:
        from src.interface.client.update_client_password_part1_ui import update_client_password_part1_ui
        from src.interface.client.client_data_account_ui import client_data_account_ui
        from src.service.send_email import token

        code = entry_code.get()
        
        if not code:
            messagebox.showerror("Error", "Introduce el codigo.")
        elif int(code) == token:
            if update_password(new_password, auth_validator.client_id):
                messagebox.showinfo("Cambio exitoso", "Su contraseña fue actualizada con exito.")
                client_data_account_ui(root)
            else:
                messagebox.showerror("Error", "Hubo un error en la actualizacion de su contraseña, vuelva a intentarlo de nuevo.")
                update_client_password_part1_ui(root)
        else:
            messagebox.showerror("Error", "El codigo es incorrecto.")
    
    except Exception as error:
        log_error(error)