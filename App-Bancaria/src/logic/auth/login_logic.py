from src.database.validation.auth_validator import validate_login
from src.utils.error_handler import log_error
from tkinter import messagebox

def login_logic(root, entry_cedula, entry_client_password):
    try:
        client_cedula = entry_cedula.get()
        client_password = entry_client_password.get()

        error_message = None

        if not client_cedula and not client_password:
            error_message = "Debes de rellenar todos los campos."
        elif not client_cedula:
            error_message = "Debes colocar tu cedula."
        elif not client_password:
            error_message = "Debes colocar tu contraseña."

        if error_message:
            messagebox.showerror("Error", error_message)
        elif validate_login(client_cedula, client_password):
            from src.interface.home.dashboard_ui import dashboard_ui
            dashboard_ui(root)
        else:
            messagebox.showerror("Error", "Cedula o contraseña incorrecto.")

    except Exception as error:
        log_error(error)