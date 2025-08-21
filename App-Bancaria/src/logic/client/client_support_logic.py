from src.database.crud.read.client_data_read import get_client_data
from src.service.send_email_support import send_email_support
from src.database.validation import auth_validator
from src.utils.error_handler import log_error
from tkinter import messagebox

def client_support_logic(root, entry_full_name, entry_case, entry_description):
    try:
        
        client_data = get_client_data(auth_validator.client_id)
        client_email = client_data["client_email"]

        client_name = entry_full_name.get()
        client_case = entry_case.get()
        description = entry_description.get()

        if not client_name and not client_case and not description:
            messagebox.showerror("Error", "Para pedir ayuda, primero debes de rellenar todos los campos.")
        elif not client_name or not client_case or not description:
            messagebox.showerror("Error", "Para pedir ayuda, primero debes de rellenar todos los campos.")
        else:  
            if send_email_support(client_name, client_case, description, client_email):
                messagebox.showinfo("Enviado con exito", "Mensaje enviado con exito, el soporte puede demorar en responder, mientras tanto este pendiente a tu correo electronico.")
            else:
                messagebox.showerror("Error al enviar", "Ocurrio un error al enviar el mensaje de ayuda, vuelva a intarlo mas tarde.")

    except Exception as error:
        log_error(error)