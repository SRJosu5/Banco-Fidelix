import random

from src.database.crud.create.bank_account_creator import create_bank_account
from src.database.crud.read.client_data_read import get_client_data
from src.utils.error_handler import log_error
from src.session import session_data 
from tkinter import messagebox

def bank_account_generator_logic(selected_bank_account_type):
    try:
        client_data = session_data.client_data
        client_phone_number = client_data["client_phone_number"]
        
        if selected_bank_account_type.get() == "Cuenta de ahorro":
            bank_account_type = "Ahorro"
        elif selected_bank_account_type.get() == "Cuenta corriente":
            bank_account_type = "Corriente"

        account_holder_name = client_data["account_holder_name"]

        random_iban_number = random.randint(10000000000000000000, 99999999999999999999)
        client_iban = f"CR{random_iban_number}"
        
        if create_bank_account(account_holder_name, bank_account_type, client_iban, client_phone_number, session_data.client_id):
            messagebox.showinfo("Cuenta bancaria creada", client_iban)
        else:
            messagebox.showerror("Error", "Ya tienes una cuenta creada, no puedes hacer otra.")

    except Exception as error:
        log_error(error)