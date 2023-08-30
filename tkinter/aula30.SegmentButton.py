import customtkinter as ctk #ok

window = ctk.CTk() #ok

window.title('App Teste') #ok
window.geometry('700x400') #ok

def botao(value):
    print('Está no segmento: ', value)




lb1 = ctk.CTkLabel(window,
                   text='Segment Button',
                   text_color='#fff',
                   width=20,
                   height=20,
                   font=('arial bold',18)).pack(pady=10,padx=10)


segment = ctk.CTkSegmentedButton(window,
                                 values=['Tkinter','Django','Flask'],
                                 command=botao,
                                 fg_color='teal',
                                 selected_color='red',
                                 selected_hover_color='green',
                                 border_width=5,
                                 width=10,
                                 corner_radius=30,
                                 unselected_color='blue',
                                 unselected_hover_color='yellow')



segment.pack(pady=20)
segment.set('Django')









window.mainloop()