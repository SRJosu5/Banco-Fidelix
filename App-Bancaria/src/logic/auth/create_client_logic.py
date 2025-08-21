from src.database.crud.create.client_creator import create_client
from src.utils.error_handler import log_error
from tkinter import messagebox

def create_client_logic(root, entry_account_holder_name, entry_client_cedula, entry_client_password, entry_client_email, entry_client_phone_number, entry_client_age):
    try:
        from src.interface.auth.login_ui import login_ui

        account_holder_name = entry_account_holder_name.get()
        client_cedula = entry_client_cedula.get()
        client_password = entry_client_password.get()
        client_email = entry_client_email.get()
        client_phone_number = entry_client_phone_number.get()
        client_age = entry_client_age.get()

        if not account_holder_name and not client_cedula and not client_password and not client_email and not client_phone_number and not client_age:
            messagebox.showerror("Error", "Debes de rellenar todos los campos.")
        elif not account_holder_name or not client_cedula or not client_password or not client_email or not client_phone_number or not client_age:
            messagebox.showerror("Error", "Debes de rellenar todos los campos.")
        elif len(client_cedula) < 9 and len(client_cedula) > 10:
            messagebox.showerror("Error", "Debes de poner una cedula valida.")
        elif len(client_password) < 8:
            messagebox.showerror("Error", "la contraseña es muy corta, minimo 8 caracteres.")
        elif len(client_phone_number) < 8 and len(client_phone_number) > 9:
            messagebox.showerror("Error", "Numero de telefono invalido.")
        else:
            if create_client(account_holder_name, client_cedula, client_password, client_email, client_phone_number, client_age):
                messagebox.showinfo("Cliente creado con exito", "Cliente fue creado con exito, vuelva a ingresas con sus datos.")
                login_ui(root)
            else:
                messagebox.showerror("Error", f"El cliente {client_cedula} ya esta existe.")
                login_ui(root)

    except Exception as error:
        log_error(error)