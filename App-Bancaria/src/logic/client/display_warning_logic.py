from src.interface.client.update_client_password_part1_ui import update_client_password_part1_ui
from src.service.internet_service import is_connected
from src.utils.error_handler import log_error
from tkinter import messagebox

def display_update_password_warning_internet(root):
    try:
        if is_connected():
            update_client_password_part1_ui(root)
        else:
            answer = messagebox.askokcancel("Error", "Revisa tu conexion a wifi. Si deseas continuar pueden haber opciones que no funcionen.")
            if answer :
                update_client_password_part1_ui(root)

    except Exception as error:
        log_error(error)