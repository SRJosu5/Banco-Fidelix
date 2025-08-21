from src.components.widget_creator import clear_widgets, create_frame, create_label_field, create_label, create_button
from src.utils.error_handler import log_error
from src.theme.colors import *

def bank_account_manager_ui(root):
    try:
        from src.logic.bank_account.account.display_warning_logic import display_account_warning_logic
        from src.interface.bank_account.account.bank_account_ui import bank_account_ui
        from src.interface.home.dashboard_ui import dashboard_ui

        clear_widgets(root)

        frame = create_frame(root, Frame_color, Frame_edge)
        create_label_field(frame, Frame_color)
        create_label(frame, f"Gestionar cuenta bancaria", 20, Frame_color, Primary_txt)
        create_label(frame, "──────────────────────────────────────", 15, Frame_color, Primary_txt) 
        create_label_field(frame, Frame_color)
        create_button(frame, "Crear cuenta bancaria", 12 ,18, Button_BG, Primary_txt, Button_edge, bank_account_ui, root)
        create_label_field(frame, Frame_color)
        create_button(frame, "Ver cuenta", 12 ,18, Button_BG, Primary_txt, Button_edge, display_account_warning_logic, root)
        create_label_field(frame, Frame_color)
        create_button(frame, "Volver", 12 ,18, Button_BG, Primary_txt, Button_edge, dashboard_ui, root)
        create_label_field(frame, Frame_color)

    except Exception as error:
        log_error(error)