import customtkinter as ctk

window = ctk.CTk()
window.title('App teste')
window.geometry('700x400')

window.resizable(False,False)

ctk.CTkLabel(window,text='Curos de Custom Tkinter - Aula 18 (Radio Button)',font=('arial bold',20)).pack(pady=20)

radio_var = ctk.IntVar(value=0)

def radio_event():
    v = radio_var.get()

    if v == 1:
        print('Masculino')
    else:
        print('Feminino')
    #print(radio_var.get())





radio = ctk.CTkRadioButton(window,text='Masculino',command=radio_event,variable=radio_var,value=1)
radio2 = ctk.CTkRadioButton(window,text='Femiino',command=radio_event,variable=radio_var,value=2)


radio.pack()
radio2.pack()







window.mainloop()