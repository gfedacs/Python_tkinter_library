import customtkinter as ctk #ok

window = ctk.CTk() #ok

window.title('App Teste') #ok
window.geometry('700x400') #ok





def event():
    print('O switch está: ',switch.get())
    if switch.get() == 'Ativado':
        window._set_appearance_mode('light')
        switch.configure(bg_color='#ebebeb')
        lb1.configure(bg_color='#ebebeb')
        lb1.configure(text_color='black')
        
        
    elif switch.get() == 'Desativado':
        window._set_appearance_mode('dark')
        switch.configure(bg_color='#242424')
        lb1.configure(bg_color='#242424')
        lb1.configure(text_color='#fff')
       
    else:
        window._set_appearance_mode('System')



lb1 = ctk.CTkLabel(window,
                   text='Switch',
                   text_color='#fff',
                   width=20,
                   height=20,
                  
                   font=('arial bold',20))

lb1.pack(pady=20,padx=10)
         



switch = ctk.CTkSwitch(window,
                       text=None,
                       command=event,
                       onvalue='Ativado',
                       offvalue='Desativado',
                       width=30,
                       fg_color='teal',
                       button_length=5
                       
                       )


switch.pack(pady=30)








window.mainloop()