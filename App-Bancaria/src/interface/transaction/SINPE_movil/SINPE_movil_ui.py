from src.components.widget_creator import clear_widgets, create_frame, create_label_field, create_label, create_button, create_entry
from src.logic.transaction.SINPE_movil.SINPE_checkup_logic import SINPE_checkup_logic
from src.database.crud.read.client_bank_account_read import get_client_bank_account
from src.interface.home.dashboard_ui import dashboard_ui
from src.utils.error_handler import log_error
from src.session import session_data
from src.theme.colors import *

def SINPE_movil_ui(root):
    try:
        clear_widgets(root)
        client_bank_account_data = session_data.client_bank_account_data

        frame = create_frame(root, Frame_color, Frame_edge)
        create_label_field(frame, Frame_color)
        create_label(frame, f"SINPE Movil", 20, Frame_color, Primary_txt)
        create_label(frame, f"Saldo actual: {client_bank_account_data['client_balance']}₡", 12, Frame_color, Primary_txt)
        create_label(frame, "──────────────────────────────────────", 15, Frame_color, Primary_txt)
        create_label_field(frame, Frame_color)
        create_label(frame, "Saldo a depositar", 12, Frame_color, Primary_txt)
        entry_deposit = create_entry(frame, 25, Entry_txt, Frame_edge)
        create_label_field(frame, Frame_color)
        create_label(frame, "SINPE del destinatario", 12, Frame_color, Primary_txt)
        entry_SINPE = create_entry(frame, 25, Entry_txt, Frame_edge)
        create_label_field(frame, Frame_color)
        create_label(frame, "Motivo", 12, Frame_color, Primary_txt)
        entry_reason = create_entry(frame, 25, Entry_txt, Frame_edge)
        create_label_field(frame, Frame_color)
        create_button(frame, "Enviar SINPE", 11, 18, Button_BG3, Button_text, Button_edge, SINPE_checkup_logic, root, entry_deposit, entry_SINPE, entry_reason)
        create_label_field(frame, Frame_color)
        create_button(frame, "Volver", 11 ,18, Button_BG, Primary_txt, Button_edge, dashboard_ui, root)
        create_label_field(frame, Frame_color)

    except Exception as error:
        log_error(error)