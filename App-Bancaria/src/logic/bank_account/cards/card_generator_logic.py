import random

from src.interface.bank_account.card.card_status_ui import card_data_ui
from src.database.crud.read.client_data_read import get_client_data
from src.database.crud.create.cards_creator import create_cards
from src.database.validation import auth_validator
from src.utils.error_handler import log_error
from tkinter import messagebox

def card_generator_logic(root, card_options, selected_iban_account_type):
    try:
        random_card_number = random.randint(100000000000000, 999999999999999)
        random_cvc = random.randint(100, 999)
        random_month = random.randint(1, 12)
        random_year = random.randint(26, 36)

        payment_network = {
            "Visa": "4"+str(random_card_number),
            "Mastercard": "5"+str(random_card_number)
            }    

        final_card = int(payment_network.get(card_options.get()))

        client_data = get_client_data(auth_validator.client_id)

        account_holder_name = client_data["account_holder_name"]
        client_iban = selected_iban_account_type.get()
        client_id = auth_validator.client_id
        expires = f"{random_month}/{random_year}"

        if create_cards(account_holder_name, final_card, random_cvc, expires, client_iban, client_id):
            messagebox.showinfo("Tarjeta creada", "La tarjeta fue creada con exito.")
            card_data_ui(root)
        else:
            messagebox.showerror("Error", "La tarjeta ya fue creada, solo puedes generar 1.")
    
    except Exception as error:
        log_error(error)