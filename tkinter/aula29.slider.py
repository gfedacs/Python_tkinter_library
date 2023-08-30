import customtkinter as ctk #ok

window = ctk.CTk() #ok

window.title('App Teste') #ok
window.geometry('700x400') #ok

def slider_event(value):
    if value == 10:
        slider.configure(fg_color='red')
    else:
        slider.configure(fg_color='green')
    
    lb2.configure(text=int(value))



lb1 = ctk.CTkLabel(window,
                   text='Aula 14 -> Slides',
                   text_color='#fff',
                   width=20,
                   height=20,
                   font=('arial bold',18))
lb1.pack(pady=10,padx=10)

slider = ctk.CTkSlider(window,from_=0,
                       to=100,
                       command=slider_event,
                       width=500,
                       button_color='blue',
                       button_length=10,
                       corner_radius=10,
                       fg_color='green',
                       progress_color='#028')
slider.pack(pady=30)

lb2 = ctk.CTkLabel(window,text='',text_color='teal',font=('arial bold',18))
lb2.pack(pady=10)





window.mainloop()
