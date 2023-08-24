from tkinter import *
from functools import partial

janela = Tk()

janela.title('Tela de Login')

lb1 = Label(janela, text='Login:  ')
lb2 = Label(janela, text='Senha:  ')

bt1 = Button(janela, text="Acessar")

def logar(ed1, ed2):
    if ed1.get().isnumeric() and ed2.get().isnumeric():
        janela2 = Tk()
        
        bd4 = Label(janela2, text="Você está on")
        bd4.grid(row=0, column=0,)
        
        janela2.geometry('200x150+100+100')
        janela2.mainloop()
    else:
        janela3 = Tk()
        lb3 = Label(janela3, text="Deu erro")
        lb3.grid(row=0, column=0,)
        janela3.geometry('200x150+100+100')
        janela3.mainloop()

ed1 = Entry(janela)
ed2 = Entry(janela,show='*')

bt1 = Button(janela, text='Confirmar', command=partial(logar, ed1, ed2))


bt1.grid(row=2,column=1)

lb1.grid(row=0,column=0)

ed1.grid(row=0,column=1)


lb2.grid(row=1,column=0)
ed2.grid(row=1,column=1)

janela.mainloop()