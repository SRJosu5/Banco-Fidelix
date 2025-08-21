from src.components.widget_creator import clear_widgets, create_frame, create_label_field, create_label, create_button, create_entry
from src.interface.menu_bar.menu_layout import menu_bar_account_client
from src.utils.error_handler import log_error
from src.theme.colors import *

def update_client_password_part2_ui(root, new_password):
    try:
        from src.interface.client.update_client_password_part1_ui import update_client_password_part1_ui
        from src.logic.client.code_verification_logic import code_verification

        clear_widgets(root)
        menu_bar_account_client(root)

        frame = create_frame(root, Frame_color, Frame_edge)
        create_label_field(frame, Frame_color)
        create_label(frame, f"Cambiar contraseña de cliente", 20, Frame_color, Primary_txt)
        create_label(frame, "──────────────────────────────────────────", 15, Frame_color, Primary_txt) 
        create_label_field(frame, Frame_color)
        create_label(frame, f"Coloca el codigo que se mando a tu correo electronico asociado.", 12, Frame_color, Primary_txt)
        create_label_field(frame, Frame_color)
        create_label(frame, f"Codigo de verificacion", 12, Frame_color, Primary_txt)
        entry_code = create_entry(frame, 30, Entry_txt, Frame_edge)
        create_label_field(frame, Frame_color)
        create_button(frame, "Cambiar contraseña", 12 ,16, Button_BG2, Primary_txt, Button_edge, code_verification, root, entry_code, new_password)
        create_label_field(frame, Frame_color)
        create_button(frame, "Volver", 12 ,16, Button_BG, Primary_txt, Button_edge, update_client_password_part1_ui, root)
        create_label_field(frame, Frame_color)

    except Exception as error:
        log_error(error)