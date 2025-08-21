from src.database.validation.password_validator import validate_old_password
from src.database.crud.read.client_data_read import get_client_data
from src.utils.error_handler import log_error
from src.service.send_email import send_email
from src.session import session_data
from tkinter import messagebox

def update_client_password_logic(root, entry_old_password, entry_new_password, entry_new_password2):
    try:
        from src.interface.client.update_client_password_part2_ui import update_client_password_part2_ui

        client_data = session_data.client_data
        client_email = client_data["client_email"]
        
        old_password = entry_old_password.get()
        new_password = entry_new_password.get()
        confirmation_password = entry_new_password2.get()

        error_message = None

        if not old_password and not new_password and not confirmation_password:
            error_message = "Llena todos los campos."
        elif not old_password or not new_password or not confirmation_password:
            error_message = "Llena todos los campos."
        elif new_password != confirmation_password:
            error_message = "Las nuevas contraseñas no coinciden."
        elif old_password == new_password:
            error_message = "La contraseña no puede ser igual a la anterior."
        elif len(new_password) < 8:
            error_message = "La contraseña es muy corta, minimo 8 caracteres."
        
        if error_message:
            messagebox.showerror("Error", error_message)
        elif old_password and new_password == confirmation_password:
            if validate_old_password(old_password):
                if send_email(client_email):
                    update_client_password_part2_ui(root, new_password)
                else:
                    messagebox.showerror("Error", "Ocurrio un error y no se pudo enviar el codigo de verificacion.")
            else:
                messagebox.showerror("Error", "Contraseña antigua incorrecta.")
    
    except Exception as error:
        log_error(error)