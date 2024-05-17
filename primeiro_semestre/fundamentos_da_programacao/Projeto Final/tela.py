from customtkinter import *
from tkinter import *
from botao import *

set_appearance_mode('dark')
set_default_color_theme('dark-blue')

login = CTk()
login.title('Login do usuário')
login.geometry("500x300")

texto = CTkLabel(login, text='Fazer Login')
texto.pack(padx=10, pady=10)

email = CTkEntry(login, placeholder_text='Seu email')
email.pack(padx=10, pady=10)

senha = CTkEntry(login, placeholder_text='Sua senha', show='*')
senha.pack(padx=10, pady=10)

checkbox = CTkCheckBox(login, text='Lembrar Login')
checkbox.pack(padx=10, pady=10)

botao = CTkButton(login, text='Login', command=clique)
botao.pack(padx=10, pady=10)

login.mainloop()
