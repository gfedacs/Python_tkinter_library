import customtkinter as ctk

window = ctk.CTk()
window.title('App teste')
window.geometry('700x400')

window.resizable(False,False)



ctk.CTkLabel(window,text='Curos de Custom Tkinter - Aula 19 (Progress)',
             font=('arial bold',20)).pack(pady=20)



progress = ctk.CTkProgressBar(window,)
progress.pack(pady=20)
#progress.start()
progress.step()
progress.stop()















window.mainloop()