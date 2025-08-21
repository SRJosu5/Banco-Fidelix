from src.database.crud.update.client_envelopes_balance_update import update_client_envelopes_balance
from src.database.crud.create.envelopes_creator import create_envelopes
from src.interface.envelopes.envelopes_ui import envelopes_ui
from src.utils.error_handler import log_error
from src.session import session_data
from tkinter import messagebox

def create_envelopes_logic(root, selected_iban_account, entry_name_envelope, entry_funds):
    try:
        client_iban = selected_iban_account.get()
        name_envelope = entry_name_envelope.get()
        funds = entry_funds.get()
        client_id = session_data.client_id
        
        error_message = None

        try:
            if not name_envelope and not funds:
                error_message = "Debes de rellenar todos los campos."
            elif not name_envelope or not int(funds):
                error_message = "Debes de rellenar todos los campos."
            elif len(name_envelope) < 4:
                error_message = "El nombre es muy corto, minimo 4 caracteres."
            
            if error_message:
                messagebox.showerror("Error", error_message)
            elif create_envelopes(name_envelope, client_iban, 0, client_id) and update_client_envelopes_balance(funds, name_envelope, client_id):
                messagebox.showinfo("Sobre creado con exito", f"Tu sobre {name_envelope} fue creado con exito.")
                envelopes_ui(root)
            else:
                messagebox.showerror("Error", "No se pudo crear tu sobre.")

        except ValueError:
            messagebox.showerror("Error", "Ingresa datos validos.")

    except Exception as error:
        log_error(error)