from src.components.widget_creator import clear_widgets, create_frame, create_label_field, create_label, create_button, create_entry
from src.database.crud.read.client_bank_account_read import get_client_bank_account
from src.logic.envelopes.create_envelopes_logic import create_envelopes_logic
from src.components.select_iban_account import select_iban_account
from src.utils.error_handler import log_error
from src.session import session_data
from src.theme.colors import *

def create_envelopes_ui(root):
    try:
        from src.interface.envelopes.envelopes_ui import envelopes_ui

        clear_widgets(root)

        client_bank_account_data = session_data.client_bank_account_data

        frame = create_frame(root, Frame_color, Frame_edge)
        create_label_field(frame, Frame_color)
        create_label(frame, f"Crear sobres", 20, Frame_color, Primary_txt)
        create_label(frame, f"Saldo actual: {client_bank_account_data["client_balance"]}₡", 12, Frame_color, Primary_txt)
        create_label(frame, "──────────────────────────────────────", 15, Frame_color, Primary_txt) 
        create_label_field(frame, Frame_color)
        create_label(frame, "Seleccione la cuenta", 12, Frame_color, Primary_txt)
        selected_iban_account = select_iban_account(frame)
        create_label_field(frame, Frame_color)
        create_label(frame, "Nombre del sobre", 12, Frame_color, Primary_txt)
        entry_name_envelope = create_entry(frame, 30, Entry_txt, Frame_edge)
        create_label_field(frame, Frame_color)
        create_label(frame, "Monto", 12, Frame_color, Primary_txt)
        entry_funds = create_entry(frame, 30, Entry_txt, Frame_edge)
        create_label_field(frame, Frame_color)
        create_button(frame, "Crear", 12 ,18, Button_BG3, Primary_txt, Button_edge, create_envelopes_logic, root, selected_iban_account, entry_name_envelope, entry_funds)
        create_label_field(frame, Frame_color)
        create_button(frame, "Volver", 12 ,18, Button_BG, Primary_txt, Button_edge, envelopes_ui, root)
        create_label_field(frame, Frame_color)

    except Exception as error:
        log_error(error)