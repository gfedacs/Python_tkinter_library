import customtkinter as ctk

window = ctk.CTk()

window.title('App Teste')
window.geometry('700x400')

ctk.CTkLabel(window,text="Menu de opções - Aula 09",font=("arial bold",20)).pack(pady=20,padx=5)


ctk.CTkLabel(window,text ='Escolha o seu mês de nascimento: ',font=('arial bold',14)).pack()

mes_var = ctk.StringVar(value='Escolha o mês')

def mes_nascimento(escolha):
    print(f'O seu mês de nascimento é : {escolha}')


mes = ctk.CTkOptionMenu( window, 
                  values= [ 'Janeiro','Fev','Mar','Abril','Maio','Junho','Outros'],
                  command=mes_nascimento,
                  variable=mes_var,
                  width=250,
                  height=50,
                  corner_radius=50,
                  fg_color='red',
                  button_color='green',
                  button_hover_color='pink',
                  dropdown_fg_color='yellow',
                  dropdown_text_color='black',
                  dropdown_font=('arial bold',15),
                  dropdown_hover_color='white')


mes.pack(pady=10)




'''
mes = ctk.CTkOptionMenu( window, 
                  values= [ 'Janeiro','Fev','Mar','Abril','Maio','Junho','Outros'],command=mes_nascimento)
mes.pack(pady=10)
mes.set('Escolha o mês')'''


window.mainloop()