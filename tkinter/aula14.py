# Propriedade Sticky
from tkinter import *

janela = Tk()

lb1 = Label(janela,text='ESPAÇO',width=15,height=3,bg='blue')

lbHORIZONTAL =  Label(janela,text='horizontal',bg='yellow')


lbVERTICAL = Label(janela,text='vertical',bg='yellow')
bbVERTICAL = Label(janela,text='verticall',bg='black')


lb1.grid(row=0,column=0)
lbHORIZONTAL.grid(row=1,column=0,sticky=W)
lbVERTICAL.grid(row=0,column=1,sticky=N)
bbVERTICAL.grid(row=1,column=1,sticky=N)















janela.geometry('400x400+200+200')
janela.mainloop()
