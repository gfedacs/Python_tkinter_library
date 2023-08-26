import customtkinter as ctk

window = ctk.CTk()

window.title('App Teste')
window.geometry('700x400')

ctk.CTkLabel(window,text='Dgite o seu nome completo').pack()


# Trabalhando com Label de forma dinâmica
# 1* Introduzindo textos por inputs

#text_var = ctk.StringVar(value=input('Digite seu nome completo: '))



#lab = ctk.CTkLabel(window,
                   #textvariable=text_var,
                   #width=200,
                   #height=25,
                   #text_color='red',
                   #font=('arial bold',16))

#lab.pack(pady=10)

# 2* Introduzindo textos por entry (Forma mais prática)

def enviar ():
    t= entry.get()
    lab.configure(text=str(t))



lab = ctk.CTkLabel(window,
                   text='',
                   width=200,
                   height=25,
                   text_color='red',
                   font=('arial bold',16),
                   fg_color='#005',
                   corner_radius=10,
                   )

lab.pack(pady=10)

entry = ctk.CTkEntry(window,width=200)
entry.pack()

ctk.CTkButton(window,
              text='enviar',
              width=200,
              command=enviar).pack(pady=10)




window.mainloop()