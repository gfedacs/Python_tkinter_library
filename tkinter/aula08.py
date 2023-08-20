# Propriedade side 

# Top (superior), Bottom (inferior), Right (Direito), Left (Esquerdo)

# Vincula uma extremidade a um componente.


from tkinter import *

janela = Tk()

lb1= Label(janela, text='Right',bg='white')
lb2= Label(janela, text='Bottom',bg='white')
lb3= Label(janela, text='Left',bg='white')
lb4= Label(janela, text='top',bg='white')


lb1.pack(side=RIGHT)
lb2.pack(side=BOTTOM)
lb3.pack(side=LEFT)
lb4.pack(side=TOP)




janela['bg'] = 'black'

janela.geometry('400x400+200+200')
janela.mainloop()

