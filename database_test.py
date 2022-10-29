import pyodbc
import tkinter as tk

conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\jrvasquez3\Documents\test.accdb;')
cursor = conn.cursor()
cursor.execute('select * from test')
df = cursor.fetchall()


### date fetched by database
print(df)


### number of columns
num_of_cols = len(df[0])
print(len(df[0]))


### number of rows
num_of_rows = len(df)
print(len(df))

root = tk.Tk()
root.geometry("1000x700")


def submit(event):
    print("test click")
    return

class table:
    def __init__(self, num_of_rows, num_of_cols, data):
        self.entry = {}
        rows_ite = 0
        ite = 0
        for i in range(num_of_rows):
            for j in range(num_of_cols):
                print(ite)
                self.entry[ite] = tk.Entry(root, width=8 )
                self.entry[ite].grid(row=i, column=j)
                self.entry[ite].bind("<Down>", lambda event, a = self.entry, ite = ite: self.input_frame_down(event, a, ite, num_of_cols))
                self.entry[ite].bind("<Up>", lambda event, a = self.entry, ite = ite: self.input_frame_up(event, a, ite, num_of_cols))
                self.entry[ite].bind("<Left>", lambda event, a = self.entry, ite = ite: self.input_frame_left(event, a, ite))
                self.entry[ite].bind("<Right>", lambda event, a = self.entry, ite = ite: self.input_frame_right(event, a, ite))
                self.entry[ite].insert(tk.END, data[i][j])
                ite = ite + 1

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





tb1 = table(num_of_rows=num_of_rows, num_of_cols=num_of_cols, data=df)
tbl1 = tk.Button(text="submit", name="submit", command=submit, width=5).grid(row=12, column=1)


root.mainloop()
