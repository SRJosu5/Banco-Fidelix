from src.components.widget_creator import clear_widgets, create_frame, create_label_field, create_label, create_button, create_entry
from src.interface.menu_bar.menu_layout import menu_bar_account_client
from src.utils.error_handler import log_error
from src.theme.colors import *

def client_support_ui(root):
    try:
        from src.logic.client.client_support_logic import client_support_logic

        clear_widgets(root)

        menu_bar_account_client(root)

        frame = create_frame(root, Frame_color, Frame_edge)
        create_label_field(frame, Frame_color)
        create_label(frame, f"Soporte al cliente", 20, Frame_color, Primary_txt)
        create_label(frame, "──────────────────────────────────────────", 15, Frame_color, Primary_txt)
        create_label_field(frame, Frame_color)
        create_label(frame, f"Nombre completo", 12, Frame_color, Primary_txt)
        entry_full_name = create_entry(frame, 40, Entry_txt, Frame_edge)
        create_label_field(frame, Frame_color)
        create_label(frame, f"Asunto del problema", 12, Frame_color, Primary_txt)
        entry_case = create_entry(frame, 40, Entry_txt, Frame_edge)
        create_label_field(frame, Frame_color)
        create_label(frame, f"Descripcion del problema", 12, Frame_color, Primary_txt)
        entry_description = create_entry(frame, 40, Entry_txt, Frame_edge)
        create_label_field(frame, Frame_color)
        create_button(frame, "Enviar", 12 ,16, Button_BG3, Primary_txt, Button_edge, client_support_logic, root, entry_full_name, entry_case, entry_description)
        create_label_field(frame, Frame_color)

    except Exception as error:
        log_error(error)