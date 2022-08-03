from tkinter import *

from sympy import expand

main = Tk()
main.title("File Menu")
# main.geometry("400x400")

menubar = Menu(main)
main.config(menu=menubar)

scroll = Scrollbar(main)
text_box = Text(main, relief="flat", yscrollcommand=scroll.set)

file_menu = Menu(menubar, tearoff=0)
edit_menu = Menu(menubar, tearoff=0)
format_menu = Menu(menubar, tearoff=0)
view_menu = Menu(menubar, tearoff=0)
help_menu = Menu(menubar, tearoff=0)

menubar.add_cascade(label="File", menu=file_menu)
menubar.add_cascade(label="Edit", menu=edit_menu)
menubar.add_cascade(label="Format", menu=format_menu)
menubar.add_cascade(label="View", menu=view_menu)
menubar.add_cascade(label="Help", menu=help_menu)

file_menu.add_command(label="New     Ctrl+N")
file_menu.add_command(label="New Window     Ctrl+Shift+N")
file_menu.add_command(label="Open...              Ctrl+O")
file_menu.add_command(label="Save                 Ctrl+S")
file_menu.add_command(label="Save As...     Ctrl+Shift+N")
file_menu.add_separator()
file_menu.add_command(label="Page Setup...")
file_menu.add_command(label="Print...             Ctrl+P")
file_menu.add_separator()
file_menu.add_command(label="Exit")

text_box.pack(side=LEFT, fill=BOTH, expand=YES)
scroll.pack(side=RIGHT, fill=Y)
scroll.config(command = text_box.yview)

main.mainloop()