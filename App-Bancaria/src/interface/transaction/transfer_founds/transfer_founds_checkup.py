from src.components.widget_creator import clear_widgets, create_frame, create_label_field, create_label, create_button, create_entry
from src.database.crud.read.client_addressee_read import get_client_addressee
from src.utils.error_handler import log_error
from src.theme.colors import *

def transfer_founds_checkup_ui(root, deposit, iban_addressee, reason):
    try:
        from src.logic.transaction.transfer_founds.transfer_founds_logic import transfer_founds_logic
        from src.interface.transaction.transfer_founds.transfer_funds_ui import transfer_funds_ui

        clear_widgets(root)

        bank_account = get_client_addressee(iban_addressee)

        frame = create_frame(root, Frame_color, Frame_edge)
        create_label_field(frame, Frame_color)
        create_label(frame, f'Transferencia bancaria', 20, Frame_color, Primary_txt)
        create_label(frame, '──────────────────────────────────────', 15, Frame_color, Primary_txt)
        create_label_field(frame, Frame_color)
        create_label(frame, f'Persona destinataria:', 15, Frame_color, Primary_txt)
        create_label(frame, f'{bank_account['account_holder_name']}', 15, Frame_color, Primary_txt)
        create_label_field(frame, Frame_color)
        create_label(frame, f'Saldo a depositar:', 15, Frame_color, Primary_txt)
        create_label(frame, f'{deposit}₡', 15, Frame_color, Primary_txt)
        create_label_field(frame, Frame_color)
        create_label(frame, f'Motivo:', 15, Frame_color, Primary_txt)
        create_label(frame, f'{reason}', 15, Frame_color, Primary_txt)
        create_label_field(frame, Frame_color)
        create_button(frame, 'Transferir', 11, 18, Button_BG2, Button_text, Button_edge, transfer_founds_logic, root, deposit, iban_addressee, reason)
        create_label_field(frame, Frame_color)
        create_button(frame, 'Volver', 11 ,13, Button_BG, Primary_txt, Button_edge, transfer_funds_ui, root)
        create_label_field(frame, Frame_color)

    except Exception as error:
        log_error(error)