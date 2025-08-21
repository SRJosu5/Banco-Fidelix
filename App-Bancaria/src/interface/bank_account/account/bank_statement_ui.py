from src.components.widget_creator import clear_widgets, create_frame, create_label_field, create_label, create_button
from src.interface.bank_account.account.bank_account_manager_ui import bank_account_manager_ui
from src.database.crud.read.client_bank_account_read import get_client_bank_account
from src.utils.copy_to_clipboard import copy_iban_to_clipboard
from src.utils.error_handler import log_error
from src.session import session_data 
from src.theme.colors import *

def bank_statement_ui(root):
    try:
        clear_widgets(root)
        
        client_bank_account_data = session_data.client_bank_account_data

        frame = create_frame(root, Frame_color, Frame_edge)
        create_label_field(frame, Frame_color)
        create_label(frame, "Estado de cuenta bancaria", 20, Frame_color, Primary_txt) 
        create_label(frame, "──────────────────────────────────────", 15, Frame_color, Primary_txt) 
        create_label_field(frame, Frame_color)
        create_label(frame, f"Numero IBAN:", 12, Frame_color, Primary_txt)
        create_label(frame, f"{client_bank_account_data["client_iban"]}", 12, Frame_color, Primary_txt)
        create_label_field(frame, Frame_color)
        create_label(frame, f"Tipo de cuenta:", 12, Frame_color, Primary_txt)
        create_label(frame, f"{client_bank_account_data["client_bank_account_type"]}", 12, Frame_color, Primary_txt)
        create_label_field(frame, Frame_color)
        create_label(frame, f"Saldo actual:", 12, Frame_color, Primary_txt)
        create_label(frame, f"{client_bank_account_data["client_balance"]}₡", 12, Frame_color, Primary_txt)
        create_label_field(frame, Frame_color)
        create_button(frame, "Copiar IBAN", 12 ,13, Button_BG3, Primary_txt, Button_edge, copy_iban_to_clipboard, root)
        create_label_field(frame, Frame_color)
        create_button(frame, "Volver", 12 ,13, Button_BG, Primary_txt, Button_edge, bank_account_manager_ui, root)
        create_label_field(frame, Frame_color)

    except Exception as error:
        log_error(error)