import customtkinter as ctk
from PIL import Image
import webbrowser


window = ctk.CTk()

window.title('App Teste')
window.geometry('700x400')

img = ctk.CTkImage(light_image=Image.open('./tkinter/icons8-github-240.png'),
                   dark_image=Image.open('./tkinter/icons8-github-240.png'),
                   size=(100,100))

img1 = ctk.CTkImage(light_image=Image.open('./tkinter/youtube.png'),
                   dark_image=Image.open('./tkinter/youtube.png'),
                   size=(100,100))

def open_website(event):
    webbrowser.open("https://github.com/gfedacs")




def evento():
    print('O botão foi clicado')
    pass

#Aula 11 --> Button

ctk.CTkLabel(window,text='Curso de custom tkinter = Entry',
             font=('arial bold',20)).pack(pady=20,padx=5)


button = ctk.CTkButton(window, 
                       text='Youtube',
                       command=evento,
                       width=300,
                       height=20,
                       fg_color='transparent',
                       hover_color='green',
                       text_color='red',
                       font=('arial bold',18),
                       border_color= '#fff',
                       border_width=3,
                       border_spacing=2,
                       corner_radius=20,
                       state='normal',
                       image=img1)
button.pack(pady=30)


lb = ctk.CTkLabel(window, text='', image=img)
lb.pack(pady=20, padx=5)

lb.bind("<Button-1>", open_website)
print('teste')

window.mainloop()