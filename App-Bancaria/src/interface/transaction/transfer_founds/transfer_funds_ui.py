from src.components.widget_creator import clear_widgets, create_frame, create_label_field, create_label, create_button, create_entry
from src.logic.transaction.transfer_founds.transfer_founds_checkup_logic import transfer_founds_checkup_logic
from src.interface.home.dashboard_ui import dashboard_ui
from src.utils.error_handler import log_error
from src.session import session_data
from src.theme.colors import *

def transfer_funds_ui(root):
    try:
        clear_widgets(root)
        client_bank_account_data = session_data.client_bank_account_data
        
        frame = create_frame(root, Frame_color, Frame_edge)
        create_label_field(frame, Frame_color)
        create_label(frame, f"Transferencia bancaria", 20, Frame_color, Primary_txt)
        create_label(frame, f"Saldo actual: {client_bank_account_data['client_balance']}₡", 12, Frame_color, Primary_txt)
        create_label(frame, "──────────────────────────────────────", 15, Frame_color, Primary_txt)
        create_label_field(frame, Frame_color)
        create_label(frame, f"Saldo a depositar", 12, Frame_color, Primary_txt)
        entry_deposit = create_entry(frame, 25, Entry_txt, Frame_edge)
        create_label_field(frame, Frame_color)
        create_label(frame, f"IBAN destinatario", 12, Frame_color, Primary_txt)
        entry_iban_addressee = create_entry(frame, 25, Entry_txt, Frame_edge)
        create_label_field(frame, Frame_color)
        create_label(frame, f"Motivo", 12, Frame_color, Primary_txt)
        entry_reason = create_entry(frame, 25, Entry_txt, Frame_edge)
        create_label_field(frame, Frame_color)
        create_button(frame, "Continuar", 12, 18, Button_BG3, Primary_txt, Button_edge, transfer_founds_checkup_logic, root, entry_deposit, entry_iban_addressee, entry_reason)
        create_label_field(frame, Frame_color)
        create_button(frame, "Volver", 12 ,18, Button_BG, Primary_txt, Button_edge, dashboard_ui, root)
        create_label_field(frame, Frame_color)

    except Exception as error:
        log_error(error)