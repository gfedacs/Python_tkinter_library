# Introdução a customtkinter

import customtkinter as ctk  # Importando a biblioteca 

janela =ctk.CTk() # Criação da janela



janela._set_appearance_mode("light")

bt = ctk.CTkButton(janela,text='Olá')
bt.pack()







janela.mainloop()