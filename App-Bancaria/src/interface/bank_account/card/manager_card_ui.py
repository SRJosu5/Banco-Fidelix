from src.components.widget_creator import clear_widgets, create_frame, create_label_field, create_label, create_button
from src.interface.home.dashboard_ui import dashboard_ui
from src.utils.error_handler import log_error
from src.theme.colors import *

def manager_card_ui(root):
    try:
        from src.interface.bank_account.card.create_card_ui import create_card_ui
        from src.interface.bank_account.card.card_status_ui import card_data_ui

        clear_widgets(root)

        frame = create_frame(root, Frame_color, Frame_edge)
        create_label_field(frame, Frame_color)
        create_label(frame, f"Gestionar tarjeta", 20, Frame_color, Primary_txt)
        create_label(frame, "──────────────────────────────────────", 15, Frame_color, Primary_txt) 
        create_label_field(frame, Frame_color)
        create_button(frame, "Crear tarjeta", 12 ,18, Button_BG, Primary_txt, Button_edge, create_card_ui, root)
        create_label_field(frame, Frame_color)
        create_button(frame, "Datos de la tarjeta", 12 ,18, Button_BG, Primary_txt, Button_edge, card_data_ui, root)
        create_label_field(frame, Frame_color)
        create_button(frame, "Volver", 12 ,18, Button_BG, Primary_txt, Button_edge, dashboard_ui, root)
        create_label_field(frame, Frame_color)

    except Exception as error:
        log_error(error)