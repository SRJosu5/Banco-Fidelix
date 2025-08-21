from src.components.widget_creator import clear_widgets, create_frame, create_label_field, create_label, create_button, create_entry
from src.database.crud.read.client_phone_number_read import get_client_phone_number
from src.utils.error_handler import log_error
from src.theme.colors import *

def SINPE_checkup_ui(root, deposit, SINPE, reason):
    try:
        from src.interface.transaction.SINPE_movil.SINPE_movil_ui import SINPE_movil_ui
        from src.logic.transaction.SINPE_movil.SINPE_logic import SINPE_logic

        clear_widgets(root)

        bank_account = get_client_phone_number(SINPE)

        frame = create_frame(root, Frame_color, Frame_edge)
        create_label_field(frame, Frame_color)
        create_label(frame, f"SINPE Movil", 20, Frame_color, Primary_txt)
        create_label(frame, "──────────────────────────────────────", 15, Frame_color, Primary_txt)
        create_label_field(frame, Frame_color)
        create_label(frame, f"Persona destinataria:", 15, Frame_color, Primary_txt)
        create_label(frame, f"{bank_account["account_holder_name"]}", 15, Frame_color, Primary_txt)
        create_label_field(frame, Frame_color)
        create_label(frame, f"Saldo a depositar:", 15, Frame_color, Primary_txt)
        create_label(frame, f"{deposit}₡", 15, Frame_color, Primary_txt)
        create_label_field(frame, Frame_color)
        create_label(frame, f"Motivo:", 15, Frame_color, Primary_txt)
        create_label(frame, f"{reason}", 15, Frame_color, Primary_txt)
        create_label_field(frame, Frame_color)
        create_button(frame, "Transferir", 11, 18, Button_BG2, Button_text, Button_edge, SINPE_logic, root, deposit, SINPE, reason)
        create_label_field(frame, Frame_color)
        create_button(frame, "Volver", 11 ,18, Button_BG, Primary_txt, Button_edge, SINPE_movil_ui, root)
        create_label_field(frame, Frame_color)

    except Exception as error:
        log_error(error)