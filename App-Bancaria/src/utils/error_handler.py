import traceback

from tkinter import messagebox

def log_error(error):
    print(f"Descripción: {error}")
    traceback.print_exc()
    messagebox.showerror("Error", f"Sucedio un error en la ejecucion del programa. {error}")