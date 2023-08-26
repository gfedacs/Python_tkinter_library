import customtkinter as ctk

window = ctk.CTk()

window.title('App Teste')
window.geometry('700x400')
window.maxsize(width=900,height=550)
window.minsize(width=500,height=30)
window.resizable(width=False,height=False)

#window._set_appearance_mode('light')

#Aula 8 - Caixa de diálogo (dialog)

def abrir():
    dialog = ctk.CTkInputDialog ( title='Caixa de Diálogo',
                                text = 'Digite seu número',
                                entry_border_color = 'red',
                                )

    if dialog.get_input() == 'teste' or 'olá':
        lb2 = ctk.CTkLabel(window,text='Deu bom')
        lb2.place(x=300,y=100)
    
btn = ctk.CTkButton(window,text='Abrir caixa de diálogo',command=abrir)
btn.pack()






window.mainloop()