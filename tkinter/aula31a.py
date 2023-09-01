import customtkinter as ctk #ok

window = ctk.CTk() #ok



window.title('App Teste')
window.geometry('700x400')

lb1 = ctk.CTkLabel(window,
                  text='Curso de Customtkinter - Aula 16 (Switch)',
                  font=('arial bold',20)).pack(pady=20,padx=10)



def event():
    print('O Switch está: ', switch.get())

    if switch.get() == 'Ativado':

        ctk.set_appearance_mode('Light')

    elif switch.get() == 'Desativado' :

        ctk.set_appearance_mode('Dark')
    
    else:
        ctk.set_appearance_mode('System')

switch = ctk.CTkSwitch(window,
                       text=None,
                       command=event,
                       onvalue='Ativado',
                       offvalue='Desativado')


switch.pack(pady=30)
window.mainloop()