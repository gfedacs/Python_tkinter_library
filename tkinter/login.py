from tkinter import *

janela = Tk()


lb1 = Label(janela,text='Login:  ')
lb2 = Label(janela,text='Senha:  ')

bt1=Button(janela,text="Acessar")


ed1= Entry(janela,)
ed2= Entry(janela,)


ed1.grid(row=0,column=1)
ed2.grid(row=1,column=1)


lb1.grid(row=0,column=0)
lb2.grid(row=1,column=0)











janela.geometry('200x150+100+100')
janela.mainloop()