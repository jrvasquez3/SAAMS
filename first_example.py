from tkinter import *
from tkinter import ttk



class window_panel:
    def __init__(self, window_title, win_geometry="1500x700", background_image= "saams_main.png"):
        self = Tk()
        self.title(window_title)
        self.geometry(win_geometry)
        bg_image = PhotoImage(file= background_image)
        Canvas_image = Canvas(self, width=800, height=800 )
        Canvas_image.pack(fill="both", expand=True)
        Canvas_image.create_image(0,0, image= bg_image, anchor="nw")
        self.mainloop()

    
main_window = window_panel("Slitter Arbor Assembly Management System", "1500x700")
print("hello")






