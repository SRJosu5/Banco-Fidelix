import tkinter as tk

from src.theme.colors import *

def clear_widgets(frame):
    for widget in frame.winfo_children():
        widget.pack_forget()

def create_frame(root, bg, highlightbackground):
    frame = tk.Frame(
        root, 
        bg=bg, 
        highlightbackground=highlightbackground, 
        highlightthickness=2)
    frame.pack(pady=20, padx=20)
    return frame

def create_label_field(frame, bg):
    void = tk.Label(
        frame, 
        text="", 
        bg=bg)
    void.pack()

def create_label(frame, text, font_size, bg, fg):
    label = tk.Label(
        frame, 
        text=text, 
        font=("Arial", font_size, "bold"), 
        bg=bg, 
        fg=fg)
    label.pack()
    return label

def create_button(frame, text, font_size, button_size, bg, fg, highlightbackground, command=None, *command_args):
    button = tk.Button(
        frame,
        text=text,
        font=("Arial", font_size, "bold"),
        width=button_size,
        bg=bg,
        fg=fg,
        command=lambda: command(*command_args) if command else None,
        highlightbackground=highlightbackground,
        highlightthickness=2,
    )
    button.pack()
    return button

def create_entry(frame, width, bg, highlightbackground):
    entry = tk.Entry(
        frame, 
        font=("Arial", 11), 
        bg=bg, 
        fg="#E0E0E0", 
        width=width, 
        bd= 0, 
        highlightbackground= highlightbackground, 
        highlightthickness=2, 
        insertbackground="white",
        relief="flat")
    entry.pack()
    return entry

def create_password_entry(frame, width, bg, highlightbackground):
    entry = tk.Entry(
        frame, 
        font=("Arial", 11), 
        bg=bg, 
        fg="#E0E0E0", 
        width=width, 
        show="*", 
        bd= 0, 
        highlightbackground= highlightbackground, 
        highlightthickness=2,  
        insertbackground="white",
        relief="flat")
    entry.pack()
    return entry