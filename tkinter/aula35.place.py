import customtkinter as ctk

window = ctk.CTk()
window.title('App teste')
window.geometry('1000x500')






ctk.CTkButton(window,text='Botão 1').place(x=20,y=0)
ctk.CTkButton(window,text='Botão 2').place(x=23,y=0)





window.mainloop()