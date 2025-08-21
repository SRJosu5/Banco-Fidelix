from src.components.widget_creator import clear_widgets, create_frame, create_label_field, create_label, create_entry, create_button
from src.interface.menu_bar.menu_layout import menu_bar_register
from src.utils.error_handler import log_error
from src.theme.colors import *

def create_client_part1_ui(root):
    try:
        from src.interface.auth.create_client_part2_ui import create_client_part2_ui
        
        clear_widgets(root)

        menu_bar_register(root)

        frame = create_frame(root, Frame_color, Frame_edge)
        create_label_field(frame, Frame_color)
        create_label(frame, "Crear nuevo cliente", 20, Frame_color, Primary_txt)
        create_label(frame, "────────────────────────────────────────", 15, Frame_color, Primary_txt)
        create_label_field(frame, Frame_color)
        create_label(frame, "Nombre completo", 12, Frame_color, Primary_txt)
        entry_account_holder_name = create_entry(frame, 30, Entry_txt, Frame_edge) # El titular de la cuenta
        create_label_field(frame, Frame_color)
        create_label(frame, "Cedula", 12, Frame_color, Primary_txt)
        entry_client_cedula = create_entry(frame, 30, Entry_txt, Frame_edge) # La cedula del usuario
        create_label_field(frame, Frame_color)
        create_label(frame, "Contraseña", 12, Frame_color, Primary_txt)
        entry_client_password = create_entry(frame, 30, Entry_txt, Frame_edge) # La contraseña del cliente
        create_label_field(frame, Frame_color)
        create_button(frame, "Continuar", 12 ,13, Button_BG, Primary_txt, Button_edge, create_client_part2_ui, root, entry_account_holder_name, entry_client_cedula, entry_client_password)
        create_label_field(frame, Frame_color)

    except Exception as error:
        log_error(error)