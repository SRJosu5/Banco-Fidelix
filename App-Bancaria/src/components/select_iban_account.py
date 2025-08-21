import tkinter as tk

from src.utils.error_handler import log_error
from src.session import session_data 
from src.theme.colors import *

def select_iban_account(frame):
    try:
        client_bank_account_data = session_data.client_bank_account_data

        iban_options = [client_bank_account_data["client_iban"]]

        selected_iban_account = tk.StringVar(frame)
        selected_iban_account.set(iban_options[0])
        
        iban_options = tk.OptionMenu(frame, selected_iban_account, *iban_options)
        iban_options.config(width=24)
        iban_options.config(bg=Frame_color, fg=Primary_txt, font=("Arial", 12, "bold"), highlightbackground=Button_edge)
        iban_options.pack()

        return selected_iban_account

    except Exception as error:
        log_error(error)