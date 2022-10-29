# Author: Jose R Vasquez Perez
# email: jrvasquez221@yahoo.com


from tkinter import *
from tkinter import ttk
import global_class_func as mn
import coil_specs_table as cst



def tool_warehouse_window(root):
    print(root)
    root_tw = Toplevel(root)
    root_tw.title("SAAMS - Tool Warehouse")
    root_tw.geometry("1200x500")

    #lb1 = Label(root_tw, text="hello")

    tw_canvas_img1 = mn.bg_canvas(root_tw, "saams_main.png", 800, 800)


    nav_frame_1 = mn.frames_w(tw_canvas_img1.can, 0, 0, 10, 25, 20, "red")
    nav_frame = nav_frame_1.name
    btn11 = ttk.Button(nav_frame, text="save", command=root_tw.destroy).grid(row=1, column=1)
    btn12 = ttk.Button(nav_frame, text="Exit", command=root_tw.destroy).grid(row=1, column=3)

    tab_frame = mn.frames_w(tw_canvas_img1.can, 1, 0, 15, 5, 5, "#FFD6D7")
    tab_fra = tab_frame.name
    knife_tw = mn.Table(tab_fra, cst.knife_warehouse)
    knife_tw.button1 = ttk.Button(tab_fra, text=str("Add Row"), command= knife_tw.save_data).grid(row=90, column=0)
    

    #inventory_table = mn.Table()


