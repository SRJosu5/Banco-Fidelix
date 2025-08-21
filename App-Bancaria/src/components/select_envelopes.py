import tkinter as tk

from src.database.crud.read.client_envelopes_read import get_client_envelopes
from src.utils.error_handler import log_error
from src.session import session_data
from src.theme.colors import *

def select_envelopes(frame):
    try:
        client_envelopes_data = session_data.client_envelopes

        envelopes_options = [client_envelopes_data]

        selected_envelopes = tk.StringVar(frame)
        selected_envelopes.set(envelopes_options[0])
        
        envelopes_options = tk.OptionMenu(frame, selected_envelopes, *envelopes_options)
        envelopes_options.config(width=18)
        envelopes_options.config(bg=Frame_color, fg=Primary_txt, font=("Arial", 12, "bold"), highlightbackground=Button_edge)
        envelopes_options.pack()

        return selected_envelopes

    except Exception as error:
        log_error(error)