import customtkinter as ctk

window = ctk.CTk()

window.title('App Teste')
window.geometry('700x400')
window.maxsize(width=900,height=550)
window.minsize(width=500,height=30)
window.resizable(width=False,height=False)

#window._set_appearance_mode('light')

# Aula 05 = Frames

frame1 = ctk.CTkFrame(master=window,width=200,height=330,fg_color='teal',bg_color='transparent',
border_width=10,corner_radius=30,border_color='red').place(x=10,y=60)

frame2 = ctk.CTkFrame(master=window,width=200,height=330,fg_color='red').place(x=230,y=60)
frame3 = ctk.CTkFrame(master= window,width=200,height=330,fg_color='blue').place(x=450,y=60)



window.mainloop()