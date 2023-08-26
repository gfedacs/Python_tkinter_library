import customtkinter as ctk

window = ctk.CTk()

window.title('App Teste')
window.geometry('700x400')
window.maxsize(width=900,height=550)
window.minsize(width=500,height=30)
window.resizable(width=False,height=False)

#window._set_appearance_mode('light')

#Aula 7 - Textbox, caixa de texto

textbox = ctk.CTkTextbox(window,width=300, height=350,scrollbar_button_color='green',corner_radius=15,
scrollbar_button_hover_color='blue',border_color='red',border_width=2,fg_color='transparent',border_spacing=20,
activate_scrollbars=False)
textbox.pack()

lb1 = ctk.CTkLabel(textbox,text='Opa')


textbox.insert('0.0','Titulo do seu texto\n\n'+'Olá dev, estou aqui programando interface gráficas com custom Tkinter no canal set-escola de programação\n\n'*20)











window.mainloop()