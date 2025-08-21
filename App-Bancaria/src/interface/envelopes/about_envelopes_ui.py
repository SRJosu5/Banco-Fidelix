from src.components.widget_creator import clear_widgets, create_frame, create_label_field, create_label, create_button, create_entry
from src.database.crud.read.client_bank_account_read import get_client_bank_account
from src.components.select_envelopes import select_envelopes
from src.utils.error_handler import log_error
from src.session import session_data
from src.theme.colors import *

def about_envelopes_ui(root):
    try:
        from src.logic.envelopes.about_envelopes_logic import about_envelopes_logic
        from src.interface.envelopes.envelopes_ui import envelopes_ui

        clear_widgets(root)

        client_bank_account_data = session_data.client_bank_account_data

        frame = create_frame(root, Frame_color, Frame_edge)
        create_label_field(frame, Frame_color)
        create_label(frame, f"Administrar sobres", 20, Frame_color, Primary_txt)
        create_label(frame, f"Saldo actual: {client_bank_account_data["client_balance"]}₡", 12, Frame_color, Primary_txt)
        create_label(frame, "──────────────────────────────────────", 15, Frame_color, Primary_txt) 
        create_label_field(frame, Frame_color)
        create_label(frame, "Seleccione el sobre", 12, Frame_color, Primary_txt)
        selected_envelopes = select_envelopes(frame)
        create_label_field(frame, Frame_color)
        create_button(frame, "Abrir", 12 ,18, Button_BG3, Primary_txt, Button_edge, about_envelopes_logic, root, selected_envelopes)
        create_label_field(frame, Frame_color)
        create_button(frame, "Volver", 12 ,18, Button_BG, Primary_txt, Button_edge, envelopes_ui, root)
        create_label_field(frame, Frame_color)

    except Exception as error:
        log_error(error)