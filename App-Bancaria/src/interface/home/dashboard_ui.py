import time

from src.components.widget_creator import clear_widgets, create_frame, create_label_field, create_label, create_button
from src.interface.menu_bar.menu_layout import menu_bar_dashboard
from src.utils.error_handler import log_error
from src.session import session_data 
from src.theme.colors import *

def dashboard_ui(root):
    try:
        inicio = time.time()

        from src.logic.transaction.transfer_founds.display_warning_logic import display_transfer_founds_warning_logic
        from src.logic.transaction.SINPE_movil.display_warning_logic import display_SINPE_warning_logic
        from src.interface.bank_account.account.bank_account_manager_ui import bank_account_manager_ui
        from src.logic.bank_account.cards.display_warning_logic import display_card_warning_logic
        from src.logic.envelopes.display_warning_logic import display_envelopes_warning_logic
        from src.components.option_under_development import option_under_development

        clear_widgets(root)
        menu_bar_dashboard(root)
        
        def client_bank_account(frame):
            if not session_data.client_bank_account_data["client_iban"] == "":
                create_label_field(frame, Frame_color)
                create_label(frame, f"IBAN: {session_data.client_bank_account_data["client_iban"]} │ Saldo: {session_data.client_bank_account_data["client_balance"]}₡", 12, Frame_color, Primary_txt)
                create_label(frame, f"Tipo de cuenta: {session_data.client_bank_account_data["client_bank_account_type"]}", 12, Frame_color, Primary_txt)

        frame = create_frame(root, Frame_color, Frame_edge)
        create_label_field(frame, Frame_color)
        create_label(frame, f"{session_data.client_data["account_holder_name"]}", 20, Frame_color, Primary_txt)
        create_label(frame, "────────────────────────────────────────", 15, Frame_color, Primary_txt) 
        client_bank_account(frame)
        create_label_field(frame, Frame_color)
        create_button(frame, "Gestionar cuenta bancaria", 12 ,22, Button_BG, Primary_txt, Button_edge, bank_account_manager_ui, root)
        create_label_field(frame, Frame_color)
        create_button(frame, "Gestionar tarjeta", 12 ,22, Button_BG, Primary_txt, Button_edge, display_card_warning_logic, root)
        create_label_field(frame, Frame_color)
        create_button(frame, "Gestionar sobres", 12 ,22, Button_BG, Primary_txt, Button_edge, display_envelopes_warning_logic, root,)
        create_label_field(frame, Frame_color)
        create_button(frame, "SINPE Movil", 12 ,22, Button_BG, Primary_txt, Button_edge, display_SINPE_warning_logic, root)
        create_label_field(frame, Frame_color)
        create_button(frame, "Transferencia bancaria", 12 ,22, Button_BG, Primary_txt, Button_edge, display_transfer_founds_warning_logic, root)
        create_label_field(frame, Frame_color)

        fin = time.time()
        print(f"El menu dashboard cargo en {fin-inicio} ms")

    except Exception as error:
        log_error(error)