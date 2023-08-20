from tkinter import *

janela = Tk()

def bt_click():
    print("bt click")
    if ed1.get().isnumeric() and ed2.get().isnumeric():
        num1= int(ed1.get())
        num2= int(ed2.get())
        lb1['text'] = num1 + num2

    else:
        lb1['text'] = 'Formato inválido'

ed1 = Entry (janela,width=20)
ed1.place(x=100,y=100)

ed2 = Entry (janela,width=20)
ed2.place(x = 100, y=130)

bt1 = Button(janela,width=17,text='click here, pleaseee',command= bt_click)
bt1.place(x = 100, y =160)

lb1 = Label(text="Label1")
lb1.place(x = 100, y =190)

janela.geometry('500x500+150+150')
janela.mainloop()