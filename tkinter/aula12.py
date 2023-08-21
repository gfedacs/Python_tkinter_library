# Gerenciador de leiaute Grid
# Propriedade Row e Column

from tkinter import *

janela = Tk()


lb1 = Label( janela, text='Label 1')
lb2 = Label( janela, text='Label 2')
lb3 = Label( janela, text='Label 3')

lb1.grid(row=1,column=1)

lb2.grid(row=2,column=5)

lb3.grid(row=12,column=55)












janela.geometry('500x200+600+200')
janela.mainloop()