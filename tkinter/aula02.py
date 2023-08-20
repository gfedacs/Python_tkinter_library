# Gerenciador de leiaute place
# Define a organização dos widgets dentro de um container 

# 01 Place -> Usa coordenadas x,y.

# 02 Pack -> Empacota os componentes(widgets) na horizontal ou vertical.

# 03 Grid -> Os widgetssão inseridos num sistema de células de uma tabela. 

from tkinter import *

janela = Tk()

lb = Label(janela,text="Eai, galerinha.")

lb.place(x = 100, y = 9)



janela.geometry('300x300+200+200')

janela.mainloop()