# Author: Jose R Vasquez Perez
# email: jrvasquez221@yahoo.com


from tkinter import *
from tkinter import ttk



# Functions -------------------------------------------------------------------------------------------------------

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

# Auto-fills calculation after every keystroke and focus-out
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


def open_window():
    return


# Classes ---------------------------------------------------------------------------------------------------------

# create canvas for window
class bg_canvas:
    def __init__(self, window_name, bg_image_name, bg_width, bg_height ):
        self.bg_image = PhotoImage(file=bg_image_name)
        self.can = Canvas(window_name, width=bg_width, height= bg_height )
        self.can.pack(fill="both", expand=True)
        self.can.create_image(0,0, image= self.bg_image, anchor="nw") 

# create frame for canvas
class frames_w:
    def __init__(self, canvas_name, row_n, col_n, col_span, pad_x, pad_y, bg_color, border=True):
        if border == True:
            self.name = Frame(canvas_name, highlightbackground="red", highlightthickness=3)
        elif border == False:
            self.name = Frame(canvas_name)
        self.name.grid(row= row_n, column= col_n, columnspan= col_span, padx= pad_x, pady= pad_y)
        self.name.config(bg= bg_color)

# label name for frame
class name_label:
    def __init__(self, frame_name, text_name, row_num, unit_of_measurement="", width_box=20, disable_numeric=False):
        self.list_order = row_num
        self.entry = Entry(frame_name, width=width_box, font="Calibri")
        self.entry.grid(row=row_num, column= 2, columnspan=2, sticky="w")
        if disable_numeric == False:
            key_stroke_validation = self.entry.register(correct_int)
            self.entry.config(validate="key", validatecommand=(key_stroke_validation, '%P'))
        self.text_name = Label(frame_name, text=str(text_name) + ":", bg="#FFD6D7", font=('Calibri', 11, 'bold'))
        self.text_name.grid(row=row_num, column=0, columnspan=2, sticky="e")
        if width_box == 20:
            col_box = 4
        else:
            col_box = 3
        Label(frame_name, text=str(unit_of_measurement), anchor="w", bg="#FFD6D7", font=("Calibri", 10, "bold")).grid(row=row_num, column=col_box)
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
    def __init__(self, frame_name, command_clicked, text_name, x, y):
        ttk.Button(frame_name, text=str(text_name), command=command_clicked).grid(row=x, column=y)


# toggle button
class toggle_button:
    def __init__(self, frame_name, row_n, label_txt_on, label_txt_off, command_on, command_off):
        self.toggle_on = PhotoImage(file="toggle_right.png")
        self.toggle_off = PhotoImage(file="toggle_left.png")
        command_on = command_on
        command_off = command_off
        self.txt_off = label_txt_off
        self.txt_on = label_txt_on
        self.text_name = Label(frame_name, text=str(label_txt_on),bg="#C4DDEA" ,font=('Calibri', 11, 'bold'))
        self.text_name.grid(row=row_n, column=0, sticky="nw")
        self.toggle_btn = Button(frame_name, text=self.txt_on, image=self.toggle_on, command=lambda:self.toggle(), bd=0, relief='flat')
        self.toggle_btn.grid(row= int(row_n + 1), column=0, sticky="nw" )
        self.toggle_btn.unit = "on"

    def toggle(self):
        if self.toggle_btn.unit == "on":
            self.toggle_btn.config(image= self.toggle_off)
            self.toggle_btn.unit = "off"
            self.text_name.config(text= self.txt_off)
        else:
            self.toggle_btn.config(image= self.toggle_on)
            self.toggle_btn.unit = "on"
            self.text_name.config(text=self.txt_on)
        return

# create table on frame
class Table:
    def __init__(self, frame_name, table_list_name):
        total_rows = len(table_list_name)
        total_columns = len(table_list_name[0])
        self.entry = {}
        iteration = 0
        for i in range(total_rows):
            for j in range(total_columns):
                if i == 0:
                    self.entry[iteration] = Canvas(frame_name,height=200,width=200, bg='#FFD6D7')     #Entry(frame_name ,width=14, bg='LightSteelBlue',fg='Black', font=('Calibri', 13, 'bold'), textvariable=self.equ)
                    self.entry[iteration].grid(row=i, column=j)
                    label_col = Label(self.entry[iteration], text= str(table_list_name[i][j]), bg='#FFD6D7', font=('Calibri', 13, ''))
                    label_col.grid()
                    #self.entry[iteration].insert(END, table_list_name[i][j])
                elif i != 0 and j == total_columns - 1:
                    self.entry[iteration] = Entry(frame_name, width=14, bg='#7AE579', fg='black', font=('Calibri', 13, ''))
                    self.entry[iteration].grid(row=i, column=j)
                    self.entry[iteration].insert(END, table_list_name[i][j])
                    self.entry[iteration].bind("<Down>", lambda event, a = self.entry, ite = iteration: self.input_frame_down(event, a, ite, total_columns))
                    self.entry[iteration].bind("<Up>", lambda event, a = self.entry, ite = iteration: self.input_frame_up(event, a, ite, total_columns))
                    self.entry[iteration].bind("<Left>", lambda event, a = self.entry, ite = iteration: self.input_frame_left(event, a, ite))
                    self.entry[iteration].bind("<Right>", lambda event, a = self.entry, ite = iteration: self.input_frame_right(event, a, ite))
                else:
                    self.entry[iteration] = Entry(frame_name, width=14, fg='black', font=('Calibri', 13, ''))
                    self.entry[iteration].grid(row=i, column=j)
                    self.entry[iteration].insert(END, table_list_name[i][j])
                    key_stroke_validation = self.entry[iteration].register(correct_int)
                    self.entry[iteration].config(validate="key", validatecommand=(key_stroke_validation, '%P'))
                    self.entry[iteration].bind("<Down>", lambda event, a = self.entry, ite = iteration: self.input_frame_down(event, a, ite, total_columns))
                    self.entry[iteration].bind("<Up>", lambda event, a = self.entry, ite = iteration: self.input_frame_up(event, a, ite, total_columns))
                    self.entry[iteration].bind("<Left>", lambda event, a = self.entry, ite = iteration: self.input_frame_left(event, a, ite))
                    self.entry[iteration].bind("<Right>", lambda event, a = self.entry, ite = iteration: self.input_frame_right(event, a, ite))
                    self.entry[iteration].bind()
                iteration = iteration + 1
        self.iteration = iteration
        f_list = [5, 9, 13, 17, 21, 25, 29, 33]
        self.btn_total = ttk.Button(frame_name, text=str("Calculate"), command= lambda fa_list=f_list: self.total_tables(self, fa_list)).grid(row=90, column=total_columns - 1)
        
    def input_frame_down(object, event, a, ite, col):
        a[ite + col].focus_set()
        return
    
    def input_frame_up(object, event, a, ite, col):
        a[ite - col].focus_set()
        return

    def input_frame_left(object, event, a, ite):
        a[ite - 1].focus_set()
        return
    
    def input_frame_right(object, event, a, ite):
        a[ite + 1].focus_set()
        return

    def total_tables(self, event, factors_list):
        for each in factors_list:
            a = self.entry[each].get()
            b = self.entry[each + 1].get()
            c = float(a) * float(b)
            d = str(round(c))
            self.entry[each + 2].delete(0, END)
            self.entry[each + 2].insert(0, d)
        return
    
    def save_data(event):
        return
    
    def add_row(self, event, iteration, frame_name):
        self.entry[iteration] = Entry(frame_name, width=14, fg='black', font=('Calibri', 13, ''))

        return
