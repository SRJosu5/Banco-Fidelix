from src.components.widget_creator import clear_widgets, create_frame, create_label, create_label_field, create_password_entry, create_button, create_entry
from src.interface.menu_bar.menu_layout import menu_bar_auth
from src.logic.auth.login_logic import login_logic
from src.utils.error_handler import log_error
from src.theme.colors import *

def login_ui(root):
    try:
        clear_widgets(root)
        menu_bar_auth(root)

        frame = create_frame(root, Frame_color, Frame_edge)
        create_label_field(frame, Frame_color)
        create_label(frame, "Banco Fidélix", 20, Frame_color, Primary_txt)
        create_label(frame, "──────────────────────", 15, Frame_color, Primary_txt) 
        create_label_field(frame, Frame_color)
        create_label(frame, "Cedula", 12, Frame_color, Primary_txt)
        entry_client_cedula = create_entry(frame, 30, Entry_txt, Frame_edge)
        create_label_field(frame, Frame_color)
        create_label(frame, "Contraseña", 12, Frame_color, Primary_txt)
        entry_client_password = create_password_entry(frame, 30, Entry_txt, Frame_edge)
        create_label_field(frame, Frame_color)
        create_button(frame, "Acceder", 12, 14, Button_BG3, Primary_txt, Button_edge, login_logic, root, entry_client_cedula, entry_client_password)
        create_label_field(frame, Frame_color)

    except Exception as error:
        log_error(error)