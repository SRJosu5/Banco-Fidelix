from tkinter import messagebox

def about():
    messagebox.showinfo("Sobre el programa", "Version 1.0.0 | Desarollador: David Cascante Alfaro")

def quit(root):
    answer = messagebox.askokcancel("Confirmar", "¿Deseas salir realmente?")
    if answer:
        root.destroy()

def close_sesion(root):
    from src.interface.auth.login_ui import login_ui
    
    answer = messagebox.askokcancel("Confirmar", "¿Deseas cerrar sesion?")
    if answer:
        login_ui(root)
    
def dashboard_menu(root):
    from src.interface.home.dashboard_ui import dashboard_ui

    dashboard_ui(root)

def bypasslogin(root):
    from src.database.validation.auth_validator import validate_login
    from src.interface.home.dashboard_ui import dashboard_ui

    if validate_login("123456789", "admin1234"):
        dashboard_ui(root)
    else:
        messagebox.showerror("Error", "No se pudo acceder como desarollador.")