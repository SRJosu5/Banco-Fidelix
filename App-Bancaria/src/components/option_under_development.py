from src.utils.error_handler import log_error
from tkinter import messagebox

def option_under_development():
    try:
        messagebox.showwarning("Opcion en desarollo", "La opcion no esta disponible ahora mismo.")
    except Exception as error:
        log_error(error)