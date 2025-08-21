from src.components.widget_creator import clear_widgets, create_frame, create_label_field, create_label, create_button, create_entry
from src.interface.menu_bar.menu_layout import menu_bar_account_client
from src.service.internet_service import is_connected
from src.utils.error_handler import log_error
from src.theme.colors import *

def update_client_password_part1_ui(root):
    try:
        from src.logic.client.update_client_password_logic import update_client_password_logic
        from src.interface.client.client_data_account_ui import client_data_account_ui

        clear_widgets(root)

        menu_bar_account_client(root)

        frame = create_frame(root, Frame_color, Frame_edge)
        create_label_field(frame, Frame_color)
        create_label(frame, f"Cambiar contraseña de cliente", 20, Frame_color, Primary_txt)
        create_label(frame, "──────────────────────────────────────────", 15, Frame_color, Primary_txt) 
        create_label_field(frame, Frame_color)
        create_label(frame, f"Coloca la contraseña antigua, y luego pon la nueva 2 veces.", 12, Frame_color, Primary_txt)
        create_label_field(frame, Frame_color)
        create_label(frame, f"Contraseña antigua", 12, Frame_color, Primary_txt)
        entry_old_password = create_entry(frame, 30, Entry_txt, Frame_edge)
        create_label_field(frame, Frame_color)
        create_label(frame, f"Contraseña nueva", 12, Frame_color, Primary_txt)
        entry_new_password = create_entry(frame, 30, Entry_txt, Frame_edge)
        create_label_field(frame, Frame_color)
        create_label(frame, f"Contraseña nueva", 12, Frame_color, Primary_txt)
        entry_new_password2 = create_entry(frame, 30, Entry_txt, Frame_edge)
        create_label_field(frame, Frame_color)
        create_button(frame, "Continuar", 12 ,16, Button_BG3, Primary_txt, Button_edge, update_client_password_logic, root, entry_old_password, entry_new_password, entry_new_password2)
        create_label_field(frame, Frame_color)
        create_button(frame, "Volver", 12 ,16, Button_BG, Primary_txt, Button_edge, client_data_account_ui, root)
        create_label_field(frame, Frame_color)

    except Exception as error:
        log_error(error)