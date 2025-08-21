from src.components.widget_creator import clear_widgets, create_frame, create_label_field, create_label, create_button
from src.components.select_bank_account_type import select_bank_account_type
from src.utils.error_handler import log_error
from src.theme.colors import *

def bank_account_ui(root):
    try:
        from src.logic.bank_account.account.bank_account_generator_logic import bank_account_generator_logic
        from src.interface.bank_account.account.bank_account_manager_ui import bank_account_manager_ui

        clear_widgets(root)

        frame = create_frame(root, Frame_color, Frame_edge)
        create_label_field(frame, Frame_color)
        create_label(frame, f"Crear cuenta bancaria", 20, Frame_color, Primary_txt)
        create_label(frame, "──────────────────────────────────────", 15, Frame_color, Primary_txt) 
        create_label_field(frame, Frame_color)
        create_label(frame, "Seleccione el tipo de cuenta:", 12, Frame_color, Primary_txt) 
        selected_bank_account_type = select_bank_account_type(frame)
        create_label_field(frame, Frame_color)
        create_button(frame, "Crear cuenta", 12 ,13, Button_BG3, Primary_txt, Button_edge, bank_account_generator_logic, selected_bank_account_type)
        create_label_field(frame, Frame_color)
        create_button(frame, "Volver", 12 ,13, Button_BG, Primary_txt, Button_edge, bank_account_manager_ui, root)
        create_label_field(frame, Frame_color)

    except Exception as error:
        log_error(error)