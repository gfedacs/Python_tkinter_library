import customtkinter as ctk

window = ctk.CTk()

window.title('App teste')
window.geometry('700x400')


ctk.CTkLabel(window,text='Curso de custom TkInter - Aula 17 (Check Box)',
             font=('arial bold',20)).pack(pady=20)


check_var=ctk.StringVar(value='off')

def checkvalue():
    v = check_var.get()
    if v == 'on':
        ctk.set_appearance_mode('Light')
    else:
        ctk.set_appearance_mode('dark')


checkbox = ctk.CTkCheckBox(window,
                           text='CheckBox',
                             variable = check_var,
                               onvalue='on',offvalue='off',
                               command=checkvalue
                               )


checkbox.pack(pady=10)





window.mainloop()