from tkinter import *

root = Tk()


class name_label:
    def __init__(self, text_name, data_type, list_order):
        self.text_name = text_name
        self.data_type = data_type
        self.list_order = list_order
        self.entry = Entry(root)
        self.entry.grid(row=list_order, column= 3)
        Label(root, text=str(text_name) + ":").grid(row=list_order)
        



label1 = name_label("SAP Batch #", "integer", 1)
label2 = name_label("Customer", "character", 2)
label3 = name_label("Width", "integer", 3)
label4 = name_label("Gauge", "integer", 4)


    
    



root.mainloop()
