import os, tkinter as tk

from src.database.crud.create.client_creator import create_client 
from src.database.setup.setup_database import create_database   
from src.interface.auth.login_ui import login_ui  
from src.utils.error_handler import log_error
from src.theme.colors import *             

def start_app():
    try:
        root = tk.Tk()
        root.title("Banco Fidelix")
        root.state("zoomed")
        root.minsize(854,600)
        root.configure(bg=Background)

        icon = os.path.join(os.path.dirname(__file__), "assets", "icon", "icon.ico")
        root.iconbitmap(icon)

        login_ui(root)
        root.mainloop()

    except Exception as error:
        log_error(error)

if __name__ == "__main__":
    os.system("cls")
    create_database()
    create_client("Cuenta desarollador", "123456789", "admin1234", "ctp.david.dev@gmail.com", "12345678", "18")
    start_app()