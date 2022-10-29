# Author: Jose R Vasquez Perez
# email: jrvasquez221@yahoo.com


# importing tkinter and other modules
from tkinter import *
from tkinter import ttk
#import sv_ttk
import global_class_func as mn
import main_order_input as mop
import Tool_Warehouse as tw

# creation of main windows
#-----------------------------------------------------------------------------------------------

# creation of window: root
root = Tk()
root.title("Slitter Arbor Assembly Management System")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
#root.geometry("%dx%d" % (screen_width, screen_height))
root.geometry("1500x700")
root.config(background="#C4DDEA")


   
# root: Canvas creation
Canvas_image1 = mn.bg_canvas(root, "saams_main.png", 800, 800)
Canvas_image = Canvas_image1.can



# root: Canvas_image: frames creation
nav_frame_1 = mn.frames_w(Canvas_image, 0, 0, 10, 25, 20, "red")
nav_frame = nav_frame_1.name
input_frame1 = mn.frames_w(Canvas_image, 1, 0, 7, 10, 3, "#FFD6D7")
input_frame = input_frame1.name
toggle_frame1 = mn.frames_w(Canvas_image, 1, 8, 3, 6, 2, "#C4DDEA", border=False)
toggle_frame = toggle_frame1.name


# root: Canvas image: toggle_frame: Toggle button creation
toggle_btn1 = mn.toggle_button(toggle_frame, 1, "Units: mm", "Units: in", "toggle", "toggle")
toggle_btn2 = mn.toggle_button(toggle_frame, 3, "Autofill: ON", "Autofill: OFF", "toggle", "toggle")



#sv_ttk.set_theme("light")


# Functions
#----------------------------------------------------------------------------------------

# button commands
def submit_click():
    sap_batch = label1.entry.get()
    customer = label2.entry.get()
    width = label3.entry.get()
    gauge = round(float(label4.entry.get()), 2)
    clearance = round(float(label6.entry.get()), 2)
    values = [sap_batch, customer, width, gauge, clearance]
    if all(values) == True and clearance != 0 and gauge != 0:
        print("all values are good - full")
        print(clearance)
        print(gauge)
        mop.order_input_frame_creation(Canvas_image, 1, 13, 7, 20 ,1, "#FFD6D7")
    else:
        print(clearance)
        print(gauge)
        print("There is at least one empty box")
    return

def clear_btn():
    label1.entry.delete(0, END)
    label2.entry.delete(0, END)
    label3.entry.delete(0, END)
    label4.entry.delete(0, END)
    label5.entry.delete(0, END)
    label6.entry.delete(0, END)
    return





# Objects in window - buttons, labels, boxes, etc.
# ----------------------------------------------------------------------------------------------------------

# main app navigator (ex. File, Options, Save, Exit, etc.)
btn_np = ttk.Button(nav_frame, text="New_Project").grid(row=1, column=0)
btn_save = ttk.Button(nav_frame, text="save", command= clear_btn).grid(row=1, column=1)
btn_tw = ttk.Button(nav_frame, text="Tool Warehouse", command= lambda root=root: tw.tool_warehouse_window(root)).grid(row=1, column=2)
btn_exit = ttk.Button(nav_frame, text="Exit", command=root.destroy).grid(row=1, column=3)



label1 = mn.name_label(input_frame, "SAP Batch #", row_num=2)
label2 = mn.name_label(input_frame, "Customer", row_num=3, disable_numeric=True)
label3 = mn.name_label(input_frame, "Width", row_num=4, unit_of_measurement="mm", width_box=10)
label4 = mn.name_label(input_frame, "Gauge", row_num=5,unit_of_measurement="mm", width_box=10)
label5 = mn.name_label(input_frame, "Cutting Gap %", row_num=6,unit_of_measurement="%", width_box=10)
label6 = mn.name_label(input_frame, "Clearance", row_num=7, unit_of_measurement="mm", width_box=10)

label3.entry.insert(0, 0)
label4.entry.insert(0, 0)
label5.entry.insert(0, 0)
label6.entry.insert(0, 0)
label4.entry.bind("<KeyRelease>", lambda event, label_num=label4, box_sec=label5, out=label6: mn.calculator_key_release(event, "mult", label_num , box_sec, out))
label5.entry.bind("<KeyRelease>", lambda event, label_num=label5, box_sec=label4, out=label6: mn.calculator_key_release(event, "mult", label_num , box_sec, out))
label6.entry.bind("<KeyRelease>", lambda event, label_num=label6, box_sec=label4, out=label5: mn.calculator_key_release(event, "div", label_num , box_sec, out))



# buttons
Clear_btn = mn.main_button(input_frame, clear_btn, "clear", 8, 2)
Submit_btn = mn.main_button(input_frame, submit_click, "Submit", 8, 3)



root.mainloop()
