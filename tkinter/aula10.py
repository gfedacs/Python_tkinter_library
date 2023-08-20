# Propriedade fill

from tkinter import *

janela = Tk()


lb1 = Label (janela, text='Horizontal',bg ='white')
lb2 = Label (janela, text='',bg ='black')
lb3 = Label (janela, text='',bg ='black')

lb1.pack(side = TOP,fill = BOTH,expand=1)


lb2.pack(side = LEFT,fill = X)

lb3.pack(side = RIGHT,fill = Y)













janela.geometry('400x400+200+200')
janela.mainloop()