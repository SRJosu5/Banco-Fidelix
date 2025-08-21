from src.interface.client.client_support_ui import client_support_ui
from src.service.internet_service import is_connected
from src.utils.error_handler import log_error
from tkinter import messagebox

def display_support_warning_internet(root):
    try:
        if is_connected():
            client_support_ui(root)
        else:
            answer = messagebox.askokcancel("Error", "Revisa tu conexion a wifi. Si deseas continuar pueden haber opciones que no funcionen.")
            if answer:
                client_support_ui(root)

    except Exception as error:
        log_error(error)