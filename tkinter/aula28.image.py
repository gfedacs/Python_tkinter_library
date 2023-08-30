import customtkinter as ctk
from PIL import Image



window = ctk.CTk()

window.title('App Teste')
window.geometry('700x400')

lb1 = ctk.CTkLabel(window,
                   text='Aula 13 -> Imagens !.!',
                   text_color='#fff',
                   width=20,
                   height=20,
                   font=('arial bold',18)).pack(pady=10,padx=10)


img1=ctk.CTkImage(light_image=Image.open('./tkinter/youtube.png'),
                  dark_image=Image.open('./tkinter/youtube.png'),
                  size=(250,250))




lb2 = ctk.CTkLabel(window,text=None,image=img1).pack(pady=10)









window.mainloop()