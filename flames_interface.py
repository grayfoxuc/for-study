import tkinter as tk
import ttkbootstrap as ttk
from Flames import *


def output():
    if not entry1_var.get() or not entry2_var.get():
        result_var.set(value="I need names!")
    else:
        result_var.set(value=compute_destiny(entry1_var.get(), entry2_var.get()))


# create a main window
window = ttk.Window(themename="darkly")
window.title("Know Your Destiny")
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
width = 500
height = 300
x_center = int((screen_width / 2) - (width / 2))
y_center = int((screen_height / 2) - (height / 2))
window.geometry(f"{width}x{height}+{x_center}+{y_center}")
window.resizable(False, False)

# create tk variables
entry1_var = tk.StringVar()
entry2_var = tk.StringVar()
result_var = tk.StringVar()

# create widgets
frame = ttk.Frame(window).pack(pady=10)
name_label1 = ttk.Label(frame, text="Enter Name 1:").pack()
entry1 = ttk.Entry(frame, textvariable=entry1_var).pack(pady=5)
name_label2 = ttk.Label(frame, text="Enter Name 2:").pack()
entry2 = ttk.Entry(frame, textvariable=entry2_var).pack(pady=5)
result_button = ttk.Button(frame, text="FLAMES", command=output).pack(pady=10)
result_label = ttk.Label(
    frame, text="Output", font="Calibri 24", textvariable=result_var
).pack(pady=5)


# window mainloop
window.mainloop()
