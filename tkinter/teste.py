import customtkinter as ctk
import webbrowser
from tkinter import *
from PIL import Image

class ClickableLabel(ctk.CTkLabel):
    def __init__(self, master, image, url, **kwargs):
        super().__init__(master, image=image, **kwargs)
        self.url = url
        self.bind("<Button-1>", self.open_website)
        self.cursor = "hand2"  # Adicione um cursor de mão para indicar que é clicável

    def open_website(self, event):
        webbrowser.open(self.url)

window = ctk.CTk()

window.title('App Teste')
window.geometry('700x400')

img = ctk.CTkImage(light_image=Image.open('./tkinter/icons8-github-240.png'),
                   dark_image=Image.open('./tkinter/icons8-github-240.png'),
                   size=(100,100))

ctk.CTkLabel(window, text='Curso de custom tkinter = Entry', font=('arial bold',20)).pack(pady=20,padx=5)

button = ctk.CTkButton(window,
                       text='',
                       width=0,
                       height=0,
                       fg_color='transparent',
                       corner_radius=0,
                       state='normal',
                       image=img)
button.pack(pady=30)

lb = ClickableLabel(window, image=img, url="https://www.example.com")
lb.pack(pady=20, padx=5)

window.mainloop()