import tkinter as tk

from src.utils.error_handler import log_error
from src.theme.colors import *

def select_card_type(frame):
    try:
        card_options = ["Visa" ,"Mastercard"]

        selected_card_type = tk.StringVar(frame)
        selected_card_type.set(card_options[0])
        
        card_options = tk.OptionMenu(frame, selected_card_type, *card_options)
        card_options.config(width=11)
        card_options.config(bg=Frame_color, fg=Primary_txt, font=("Arial", 12, "bold"), highlightbackground=Button_edge)
        card_options.pack()

        return selected_card_type

    except Exception as error:
        log_error(error)