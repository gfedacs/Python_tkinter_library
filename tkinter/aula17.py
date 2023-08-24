import customtkinter as ctk

janela=ctk.CTk() #Criar a nossa janela







janela.title('App Teste')
janela.geometry('700x400')

janela.maxsize(width=100,height=500)
janela.minsize(width=500,height=250)

janela.resizable(width=True,height=False)
janela.iconify()

janela.deiconify()


janela.mainloop()