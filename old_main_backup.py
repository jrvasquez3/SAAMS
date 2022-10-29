# Author: Jose R Vasquez Perez


# importing tkinter and other modules
from tkinter import *
from tkinter import ttk
import sv_ttk

# creation of main windows
#-----------------------------------------------------------------------------------------------

# creation of window
root = Tk()
root.title("Slitter Arbor Assembly Management System")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
#root.geometry("%dx%d" % (screen_width, screen_height))
root.geometry("1500x700")


# background pciture on main
bg_image = PhotoImage(file="C:\\Users\\jrvas\\Desktop\\CASKA_Replacement\\slitter-arbor-assembly-management-system\\saams_main.png")
Canvas_image = Canvas(root, width=800, height=800 )
Canvas_image.pack(fill="both", expand=True)
Canvas_image.create_image(0,0, image= bg_image, anchor="nw")

# nav menu
nav_frame = Frame(Canvas_image, highlightbackground="red", highlightthickness=3)
nav_frame.grid(row=0, column=0, columnspan=7, padx=25, pady=20)
nav_frame.config(bg="red")

# input boxes frame
input_frame = Frame(Canvas_image, highlightbackground="red", highlightthickness=3)
input_frame.grid(row=1, column=0, columnspan=7, padx=10, pady=3)
input_frame.config(bg="#FFD6D7")

#sv_ttk.set_theme("light")




# Functions
#----------------------------------------------------------------------------------------



# button commands
def submit_click():
    sap_batch = label1.entry.get()
    customer = label2.entry.get()
    width = label3.entry.get()
    gauge = label4.entry.get()
    print(sap_batch)
    print(customer)
    print(width)
    print(gauge)
    return

def clear_btn():
    label1.entry.delete(0, END)
    label2.entry.delete(0, END)
    label3.entry.delete(0, END)
    label4.entry.delete(0, END)
    label5.entry.delete(0, END)
    label6.entry.delete(0, END)
    return


# Internal Functions 
#---------------------------------------------------------------------------------------------------

# Allows only numbers and floats to be typed into entry, not strings
def correct_int(key_val):
    # Check if keys is numberic
    if key_val.isnumeric():
        return True
    # Check if keys is empty
    elif key_val == "":
        return True
    else:
        # Check if keys is float 
        try:
            float_test = float(key_val)
        except ValueError:
            float_test = key_val
        if isinstance(float_test, float) == True:
            return True
        # test fails. Prevents key from being typed into box
        else:
            return False





def calculator_key_release(event, operation ,box_label_num, box_2,output_box):
    gap_per = box_label_num.entry.get()
    box2 = box_2.entry.get()
    if gap_per == "":
        output_box.entry.delete(0, END)
        output_box.entry.insert(0, 0)
        return
    if box2 == "":
        box_2.entry.insert(0, 0)
        box2 = box_2.entry.get()
    if operation == "mult":
        resultant = (float(gap_per)/100) * (float(box2))
        output_box.entry.delete(0, END)
        output_box.entry.insert(0, round(resultant, 2))
    elif operation == "div":
        try:
            resultant = ((float(gap_per))* 100)/(float(box2))
        except ZeroDivisionError:
            resultant = 0
        output_box.entry.delete(0, END)
        output_box.entry.insert(0, round(resultant, 2))
    return







# Classes - Object Creation
#---------------------------------------------------------------------------------------

# create Input Entry Box, and name of its label
class name_label:
    def __init__(self, text_name, row_num, unit_of_measurement="", width_box=20, disable_numeric=False):
        self.list_order = row_num
        self.entry = Entry(input_frame, width=width_box, font="Calibri")
        self.entry.grid(row=row_num, column= 2, columnspan=2, sticky="w")
        if disable_numeric == False:
            key_stroke_validation = self.entry.register(correct_int)
            self.entry.config(validate="key", validatecommand=(key_stroke_validation, '%P'))
        self.text_name = Label(input_frame, text=str(text_name) + ":", bg="#FFD6D7", font=('Calibri', 11, 'bold'))
        self.text_name.grid(row=row_num, column=0, columnspan=2, sticky="e")
        if width_box == 20:
            col_box = 4
        else:
            col_box = 3
        Label(input_frame, text=str(unit_of_measurement), anchor="w", bg="#FFD6D7", font=("Calibri", 10, "bold")).grid(row=row_num, column=col_box)
        self.entry.bind("<Down>", self.input_frame_down)
        self.entry.bind("<Up>", self.input_frame_up)

    def input_frame_down(object, event):
        event.widget.tk_focusNext().focus_set()
        return
    
    def input_frame_up(object, event):
        event.widget.tk_focusPrev().focus_set()
        return
    






# create button
class main_button:
    def __init__(self, command_clicked, text_name, x, y):
        ttk.Button(input_frame, text=str(text_name), command=command_clicked).grid(row=x, column=y)




# Objects in window - buttons, labels, boxes, etc.
# ----------------------------------------------------------------------------------------------------------

# main app navigator (ex. File, Options, Save, Exit, etc.)
ttk.Button(nav_frame, text="New_Project").grid(row=1, column=0)
ttk.Button(nav_frame, text="save", command=submit_click).grid(row=1, column=1)
ttk.Button(nav_frame, text="Exit", command=root.destroy).grid(row=1, column=2)

# text fields enter
label1 = name_label("SAP Batch #", row_num=2)
label2 = name_label("Customer", row_num=3, disable_numeric=True)
label3 = name_label("Width", row_num=4, unit_of_measurement="mm", width_box=10)
label4 = name_label("Gauge", row_num=5,unit_of_measurement="mm", width_box=10)
label5 = name_label("Cutting Gap %", row_num=6,unit_of_measurement="%", width_box=10)
label6 = name_label("Clearance", row_num=7, unit_of_measurement="mm", width_box=10)

label3.entry.insert(0, 0)
label4.entry.insert(0, 0)
label5.entry.insert(0, 0)
label6.entry.insert(0, 0)
label4.entry.bind("<KeyRelease>", lambda event, label_num=label4, box_sec=label5, out=label6: calculator_key_release(event, "mult", label_num , box_sec, out))
label5.entry.bind("<KeyRelease>", lambda event, label_num=label5, box_sec=label4, out=label6: calculator_key_release(event, "mult", label_num , box_sec, out))
label6.entry.bind("<KeyRelease>", lambda event, label_num=label6, box_sec=label4, out=label5: calculator_key_release(event, "div", label_num , box_sec, out))



# buttons
Clear_btn = main_button(clear_btn, "clear", 8, 2)
Submit_btn = main_button(submit_click, "Submit", 8, 3)



root.mainloop()
