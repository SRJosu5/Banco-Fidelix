import tkinter as tk

from src.utils.error_handler import log_error
from src.theme.colors import *

def select_bank_account_type(frame):
    try:
        bank_optios_options = ["Cuenta de ahorro" ,"Cuenta corriente"]

        selected_bank_account_type = tk.StringVar(frame)
        selected_bank_account_type.set(bank_optios_options[0])
        
        bank_optios_options = tk.OptionMenu(frame, selected_bank_account_type, *bank_optios_options)
        bank_optios_options.config(width=15)
        bank_optios_options.config(bg=Frame_color, fg=Primary_txt, font=("Arial", 12, "bold"), highlightbackground=Button_edge)
        bank_optios_options.pack()

        return selected_bank_account_type

    except Exception as error:
        log_error(error)