import customtkinter as ctk

window = ctk.CTk()

window.title('App')

window.geometry('700x400')

def criar_janela():
    newindow = ctk.CTkToplevel(window,fg_color='red')
    newindow.geometry('700x400')
    window.mainloop()



bt1 = ctk.CTkButton(master=window,text='Gerar janela',command=criar_janela).place(x=300,y=100)





window.mainloop()