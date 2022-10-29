from tkinter import *
from tkinter import ttk
import global_class_func as mn
import coil_specs_table as cst


def order_input_frame_creation(canvas_name, row_n, col_n, col_span, pad_x, pad_y, bg_color):
    order_input_frame1 = mn.frames_w(canvas_name, row_n, col_n, col_span, pad_x, pad_y, bg_color)
    order_input_frame = order_input_frame1.name
    order_table = mn.Table(order_input_frame, cst.coil_specifications)
    #factor_list_var1 = [5, 9, 13, 17, 21, 25, 29, 33]
    #order_table_btn = mn.main_button(order_input_frame, mn., "Calculate", 90, 3)
    return









