import customtkinter as ctk
from tkinter import *

window = ctk.CTk()

window.title('App Teste')
window.geometry('700x400')

def pegar():
    print(entry.get())
    entry.delete(0,END)
    


'''
def apagar():
    entry.delete(0,END)

ctk.CTkButton(window,
              width=300,
              text='Apagar texto',
              command=apagar).pack(pady=5)
'''

ctk.CTkLabel(window,text='Curso de custom tkinter = Entry',
             font=('arial bold',20)).pack(pady=20,padx=5)




entry = ctk.CTkEntry(window,
                     width=300,
                     placeholder_text='Digite o seu nome completo...',
                     placeholder_text_color='green',
                     fg_color='transparent',
                     text_color='teal',
                     font=('arial bold',16),
                     border_width=2,
                     border_color='#fff',
                     state='normal',
                     corner_radius=50) #disabled

entry.pack(pady=20)

ctk.CTkButton(window,
              width=300,
              text='Pegar texto',
              command=pegar).pack()














window.mainloop()