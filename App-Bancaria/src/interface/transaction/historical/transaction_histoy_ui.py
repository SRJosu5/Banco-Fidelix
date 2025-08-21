from components.widget_creator import clear_widgets, create_frame, create_label_field, create_label, create_button
from interface.menu_bar.menu_layout import menu_bar_dashboard
from utils.error_handler import log_error
from theme.colors import *

def transaction_histoy_ui(root):
    try:
        clear_widgets(root)
        menu_bar_dashboard(root)
    except Exception as error:
        log_error(error)