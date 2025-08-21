import tkinter as tk

from src.interface.menu_bar.menu_events import about, quit, close_sesion, dashboard_menu, bypasslogin
from src.utils.error_handler import log_error

def menu_bar_dashboard(root):
    try:
        from src.logic.client.display_support_warning_logic import display_support_warning_internet
        from src.interface.client.client_data_account_ui import client_data_account_ui
        from src.components.option_under_development import option_under_development

        menu_bar = tk.Menu(root)
        root.config(menu=menu_bar)

        menu_sesion = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Sesion de cliente", menu=menu_sesion)
        menu_sesion.add_command(label="Cerrar sesion", command=lambda: close_sesion(root))
        menu_sesion.add_separator()
        menu_sesion.add_command(label="Datos de cuenta", command=lambda: client_data_account_ui(root))
        menu_sesion.add_separator()
        menu_sesion.add_command(label="Menu principal", command=lambda: dashboard_menu(root))
        menu_sesion.add_separator()
        menu_sesion.add_command(label="Historial", command=lambda: option_under_development())
        menu_sesion.add_separator()
        menu_sesion.add_command(label="Soporte al cliente", command=lambda: display_support_warning_internet(root))

        menu_help = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Informacion", menu=menu_help)
        menu_help.add_command(label="Acerda de", command=lambda: about())

        menu_quit = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Salir", menu=menu_quit)
        menu_quit.add_cascade(label="Salir del programa", command=lambda: quit(root))
    
    except Exception as error:
        log_error(error)

def menu_bar_auth(root):
    try:
        from src.interface.auth.create_client_part1_ui import create_client_part1_ui
        
        menu_bar = tk.Menu(root)
        root.config(menu=menu_bar)

        menu_register = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Cliente", menu=menu_register)
        menu_register.add_command(label="Crear nuevo cliente", command=lambda: create_client_part1_ui(root))
        menu_register.add_separator()
        menu_register.add_command(label="Iniciar sesion como desarollador", command=lambda: bypasslogin(root))

        menu_help = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Informacion", menu=menu_help)
        menu_help.add_command(label="Acerda de", command=lambda: about())

        menu_quit = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Salir", menu=menu_quit)
        menu_quit.add_cascade(label="Salir del programa", command=lambda: quit(root))

    except Exception as error:
        log_error(error)

def menu_bar_register(root):
    try:
        from src.interface.auth.login_ui import login_ui

        menu_bar = tk.Menu(root)
        root.config(menu=menu_bar)

        menu_back = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Iniciar sesion", menu=menu_back)
        menu_back.add_command(label="Volver al login", command=lambda: login_ui(root))
        menu_back.add_separator()
        menu_back.add_command(label="Iniciar sesion como desarollador", command=lambda: bypasslogin(root))

        menu_help = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Informacion", menu=menu_help)
        menu_help.add_command(label="Acerda de", command=lambda: about())

        menu_quit = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Salir", menu=menu_quit)
        menu_quit.add_cascade(label="Salir del programa", command=lambda: quit(root))

    except Exception as error:
        log_error(error)

def menu_bar_account_client(root):
    try:
        from src.logic.client.display_support_warning_logic import display_support_warning_internet
        from src.components.option_under_development import option_under_development

        menu_bar = tk.Menu(root)
        root.config(menu=menu_bar)

        menu_sesion = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Sesion de cliente", menu=menu_sesion)
        menu_sesion.add_command(label="Cerrar sesion", command=lambda: close_sesion(root))
        menu_sesion.add_separator()
        menu_sesion.add_command(label="Menu principal", command=lambda: dashboard_menu(root))
        menu_sesion.add_separator()
        menu_sesion.add_command(label="Historial", command=lambda: option_under_development())
        menu_sesion.add_separator()
        menu_sesion.add_command(label="Soporte al cliente", command=lambda: display_support_warning_internet(root))

        menu_help = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Informacion", menu=menu_help)
        menu_help.add_command(label="Acerda de", command=lambda: about())

        menu_quit = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Salir", menu=menu_quit)
        menu_quit.add_cascade(label="Salir del programa", command=lambda: quit(root))

    except Exception as error:
        log_error(error)