import customtkinter as ctk

window = ctk.CTk()

window.title('App Teste')
window.geometry('700x400')
window._set_appearance_mode('dark')

def soma():
    if int(ed.get().isnumeric()) and int(ed1.get().isnumeric()):
       
        resultado = int(ed.get()) + int(ed1.get())
        lb_resultado.configure(text=str(resultado))  # Substitua config por configure
    else:
        lb_resultado.configure(text=str('Valores inválidos'))

lb1 = ctk.CTkLabel(window,
                   text='Calculadora IFPB',
                   width=700,
                   height=100,
                   text_color='red',
                   corner_radius=20,
                   bg_color='black',
                   font=('arial bold', 16))
lb1.pack()

lb2 = ctk.CTkLabel(window,
                   text='Digite dois numeros, pra realizar sua adição:',
                   width=200, height=100,
                   text_color='red',
                   font=('arial bold', 16))
lb2.pack()

ed = ctk.CTkEntry(window,
                  width=100,
                  height=20,
                  corner_radius=10)
ed.pack(pady=10)

ed1 = ctk.CTkEntry(window,
                   width=100,
                   height=20,
                   corner_radius=10) 
ed1.pack(pady=10)

bt1 = ctk.CTkButton(window,
                    text='ENVIAR',
                    fg_color='transparent',
                    font=('arial bold', 20),
                    hover_color='black',
                    text_color='red',
                    command=soma)
bt1.pack()

lb_resultado = ctk.CTkLabel(window,
                            text='Aguardando resultado...',
                            width=200, height=100,
                            text_color='red',
                            font=('arial bold', 25))
lb_resultado.pack()

window.mainloop()