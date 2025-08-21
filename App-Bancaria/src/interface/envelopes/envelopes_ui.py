from src.components.widget_creator import clear_widgets, create_frame, create_label_field, create_label, create_button
from src.interface.home.dashboard_ui import dashboard_ui
from src.utils.error_handler import log_error
from src.theme.colors import *

def envelopes_ui(root):
    try:
        from src.interface.envelopes.create_envelopes_ui import create_envelopes_ui
        from src.interface.envelopes.about_envelopes_ui import about_envelopes_ui

        clear_widgets(root)

        frame = create_frame(root, Frame_color, Frame_edge)
        create_label_field(frame, Frame_color)
        create_label(frame, f"Gestionar sobres", 20, Frame_color, Primary_txt)
        create_label(frame, "──────────────────────────────────────", 15, Frame_color, Primary_txt) 
        create_label_field(frame, Frame_color)
        create_button(frame, "Crear sobres", 12 ,18, Button_BG, Primary_txt, Button_edge, create_envelopes_ui, root)
        create_label_field(frame, Frame_color)
        create_button(frame, "Administrar sobres", 12 ,18, Button_BG, Primary_txt, Button_edge, about_envelopes_ui, root)
        create_label_field(frame, Frame_color)
        create_button(frame, "Volver", 12 ,18, Button_BG, Primary_txt, Button_edge, dashboard_ui, root)
        create_label_field(frame, Frame_color)

    except Exception as error:
        log_error(error)