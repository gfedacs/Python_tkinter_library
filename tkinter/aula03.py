# Trabalho com botões e labels

from tkinter import *
def clicar():
    print("Botão clicado")

    lb["text"] = "Deu bom"


janela = Tk()

bt = Button (janela, width= 20, text = "OK",command=clicar)

bt.place(x=100,y = 100)

lb = Label(janela,text= "Eai, Ring Necks!")

lb.place(x=100,y=150)





janela.geometry('300x300+200+200')
janela.mainloop()