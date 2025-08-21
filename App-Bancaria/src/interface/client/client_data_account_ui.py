from src.components.widget_creator import clear_widgets, create_frame, create_label_field, create_label, create_button
from src.interface.menu_bar.menu_layout import menu_bar_account_client
from src.database.crud.read.client_data_read import get_client_data
from src.utils.error_handler import log_error
from src.session import session_data
from src.theme.colors import *

def client_data_account_ui(root):
    try:
        from src.logic.client.display_warning_logic import display_update_password_warning_internet

        clear_widgets(root)

        menu_bar_account_client(root)

        client_data = session_data.client_data

        frame = create_frame(root, Frame_color, Frame_edge)

        create_label_field(frame, Frame_color)
        create_label(frame, f"Datos de cliente", 20, Frame_color, Primary_txt)
        create_label(frame, "────────────────────────────────────", 15, Frame_color, Primary_txt) 
        create_label_field(frame, Frame_color)
        create_label(frame, f"Nombre completo:", 12, Frame_color, Primary_txt)
        create_label(frame, f"{client_data["account_holder_name"]}", 12, Frame_color, Primary_txt)
        create_label_field(frame, Frame_color)
        create_label(frame, f"Cedula del cliente:", 12, Frame_color, Primary_txt)
        create_label(frame, f"{client_data["client_cedula"]}", 12, Frame_color, Primary_txt)
        create_label_field(frame, Frame_color)
        create_label(frame, f"Correo registrado:", 12, Frame_color, Primary_txt)
        create_label(frame, f"{client_data["client_email"]}", 12, Frame_color, Primary_txt)
        create_label_field(frame, Frame_color)
        create_label(frame, f"Numero telefonico:", 12, Frame_color, Primary_txt)
        create_label(frame, f"{client_data["client_phone_number"]}", 12, Frame_color, Primary_txt)
        create_label_field(frame, Frame_color)
        create_label(frame, f"Edad del cliente:", 12, Frame_color, Primary_txt)
        create_label(frame, f"{client_data["client_age"]} años", 12, Frame_color, Primary_txt)
        create_label_field(frame, Frame_color)
        create_button(frame, "Cambiar contraseña", 12 ,16, Button_BG3, Primary_txt, Button_edge, display_update_password_warning_internet, root)
        create_label_field(frame, Frame_color)
        
    except Exception as error:
        log_error(error)