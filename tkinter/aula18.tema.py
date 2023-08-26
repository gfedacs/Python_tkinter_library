import customtkinter as ctk

janela=ctk.CTk() #Criar a nossa janela

#Configurando a nossa janela principal = 03


janela.title('App Teste')
janela.geometry('700x400')
janela.maxsize(width=100,height=500)
janela.minsize(width=500,height=250)
janela.resizable(width=True,height=False)


#Customizando o tema da aplicação = 03 

janela._set_appearance_mode('light')
janela._set_appearance_mode('system')

janela.mainloop()