import customtkinter as ctk

window = ctk.CTk()

window.title('App Teste')
window.geometry('700x400')
window.maxsize(width=900,height=550)
window.minsize(width=500,height=30)
window.resizable(width=False,height=False)

#window._set_appearance_mode('light')

# Aula 06 = Tabview (Abas no tkinter)

Tabview = ctk.CTkTabview(master=window, width=400,corner_radius=20,border_width=5,border_color='red',
fg_color='teal',segmented_button_fg_color='red',segmented_button_selected_color='green',
segmented_button_unselected_hover_color='blue',segmented_button_unselected_color='yellow')




Tabview.pack()
Tabview.add('Nomes')
Tabview.add('Idades')
Tabview.add('Gênero')

Tabview.tab('Nomes').grid_columnconfigure(0,weight=1)
Tabview.tab('Idades').grid_columnconfigure(0,weight=1)
Tabview.tab('Gênero').grid_columnconfigure(0,weight=1)

# Adicionando elementos na nossa tab

text = ctk.CTkLabel(Tabview.tab('Nomes'),text = 'Salvador Eduardo\n Félix\n Antonio Maia')
text.pack()

idade = ctk.CTkLabel(Tabview.tab('Idades'),text = '18\n 19\n 44')
idade.pack()

gen = ctk.CTkLabel(Tabview.tab('Gênero'),text = 'M\n F\n F')
gen.pack()











window.mainloop()