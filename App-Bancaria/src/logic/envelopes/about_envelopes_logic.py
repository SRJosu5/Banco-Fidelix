from src.database.validation import auth_validator
from src.utils.error_handler import log_error
from tkinter import messagebox

def about_envelopes_logic(root, selected_envelopes):
    try:

        envelope = selected_envelopes.get()
        print(envelope)        


    except Exception as error:
        log_error(error)