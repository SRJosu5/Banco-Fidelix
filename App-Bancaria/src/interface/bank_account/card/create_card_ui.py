from src.components.widget_creator import clear_widgets, create_frame, create_label_field, create_label, create_button
from src.components.select_iban_account import select_iban_account
from src.components.select_card_type import select_card_type
from src.utils.error_handler import log_error
from src.theme.colors import *

def create_card_ui(root):
    try:
        from src.logic.bank_account.cards.card_generator_logic import card_generator_logic
        from src.interface.bank_account.card.manager_card_ui import manager_card_ui

        clear_widgets(root)

        frame = create_frame(root, Frame_color, Frame_edge)
        create_label_field(frame, Frame_color)
        create_label(frame, f"Crear tarjeta", 20, Frame_color, Primary_txt)
        create_label(frame, "──────────────────────────────────────", 15, Frame_color, Primary_txt) 
        create_label_field(frame, Frame_color)
        create_label(frame, "Cuenta IBAN:", 12, Frame_color, Primary_txt) 
        selected_iban_account = select_iban_account(frame)
        create_label_field(frame, Frame_color)
        create_label(frame, "Tipo de metedo:", 12, Frame_color, Primary_txt) 
        selected_card_type = select_card_type(frame)
        create_label_field(frame, Frame_color)
        create_button(frame, "Crear tarjeta", 12 ,18, Button_BG3, Primary_txt, Button_edge, card_generator_logic, root, selected_card_type, selected_iban_account)
        create_label_field(frame, Frame_color)
        create_button(frame, "Volver", 12 ,18, Button_BG, Primary_txt, Button_edge, manager_card_ui, root)
        create_label_field(frame, Frame_color)        

    except Exception as error:
        log_error(error)