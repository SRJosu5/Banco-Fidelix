from src.components.widget_creator import clear_widgets, create_frame, create_label_field, create_label, create_entry, create_button
from src.logic.auth.create_client_logic import create_client_logic
from src.utils.error_handler import log_error
from src.theme.colors import *

def create_client_part2_ui(root, entry_account_holder_name, entry_client_cedula, entry_client_password):
    try:
        from src.interface.auth.create_client_part1_ui import create_client_part1_ui

        clear_widgets(root)

        frame = create_frame(root, Frame_color, Frame_edge)
        create_label_field(frame, Frame_color)
        create_label(frame, "Crear nuevo cliente", 20, Frame_color, Primary_txt)
        create_label(frame, "────────────────────────────────────────", 15, Frame_color, Primary_txt)
        create_label_field(frame, Frame_color)
        create_label(frame, "Correo electronico", 12, Frame_color, Primary_txt)
        entry_client_email = create_entry(frame, 30, Entry_txt, Frame_edge)
        create_label_field(frame, Frame_color)
        create_label(frame, "Numero de telefono", 12, Frame_color, Primary_txt)
        entry_client_phone_number = create_entry(frame, 30, Entry_txt, Frame_edge)
        create_label_field(frame, Frame_color)
        create_label(frame, "Edad", 12, Frame_color, Primary_txt)
        entry_client_age = create_entry(frame, 30, Entry_txt, Frame_edge)
        create_label_field(frame, Frame_color)
        create_button(frame, "Registrar cliente", 12 ,13, Button_BG3, Primary_txt, Button_edge, create_client_logic, root, entry_account_holder_name, entry_client_cedula, entry_client_password, entry_client_email, entry_client_phone_number, entry_client_age)
        create_label_field(frame, Frame_color)
        create_button(frame, "Volver", 12 ,13, Button_BG, Primary_txt, Button_edge, create_client_part1_ui, root)
        create_label_field(frame, Frame_color)

    except Exception as error:
        log_error(error)