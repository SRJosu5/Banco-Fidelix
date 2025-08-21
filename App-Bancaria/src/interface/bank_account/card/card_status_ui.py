from src.components.widget_creator import clear_widgets, create_frame, create_label_field, create_label, create_button
from src.database.crud.read.client_card_data_read import get_client_card_data
from src.utils.copy_to_clipboard import copy_card_to_clipboard
from src.utils.error_handler import log_error
from src.session import session_data 
from src.theme.colors import *

def card_data_ui(root):
    try:
        from src.interface.bank_account.card.manager_card_ui import manager_card_ui

        clear_widgets(root)

        client_card_data = session_data.client_card_data

        frame = create_frame(root, Frame_color, Frame_edge)
        create_label_field(frame, Frame_color)
        create_label(frame, f"Datos de la tarjeta", 20, Frame_color, Primary_txt)
        create_label(frame, "──────────────────────────────────────", 15, Frame_color, Primary_txt) 
        create_label_field(frame, Frame_color)
        create_label(frame, "Titular:", 12, Frame_color, Primary_txt) 
        create_label(frame, f"{client_card_data["account_holder_name"]}", 12, Frame_color, Primary_txt) 
        create_label_field(frame, Frame_color)
        create_label(frame, "Numero de tarjeta:", 12, Frame_color, Primary_txt) 
        create_label(frame, f"{client_card_data["card_number"]}", 12, Frame_color, Primary_txt) 
        create_label_field(frame, Frame_color)
        create_label(frame, "Codigo de seguridad:", 12, Frame_color, Primary_txt) 
        create_label(frame, f"{client_card_data["cvc"]}", 12, Frame_color, Primary_txt) 
        create_label_field(frame, Frame_color)
        create_label(frame, "Fecha de vencimiento:", 12, Frame_color, Primary_txt) 
        create_label(frame, f"{client_card_data["expires"]}", 12, Frame_color, Primary_txt) 
        create_label_field(frame, Frame_color)
        create_label(frame, "Cuenta bancaria asocieda:", 12, Frame_color, Primary_txt) 
        create_label(frame, f"{client_card_data["client_iban"]}", 12, Frame_color, Primary_txt) 
        create_label_field(frame, Frame_color)
        create_button(frame, "Copiar datos", 12 ,18, Button_BG3, Primary_txt, Button_edge, copy_card_to_clipboard, root)
        create_label_field(frame, Frame_color)
        create_button(frame, "Volver", 12 ,18, Button_BG, Primary_txt, Button_edge, manager_card_ui, root)
        create_label_field(frame, Frame_color)
    
    except Exception as error:
        log_error(error)