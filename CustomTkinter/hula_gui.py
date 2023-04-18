from logging import PercentStyle
import tkinter
import customtkinter as ct

colormode = ["dark", "light"]

ct.set_appearance_mode(colormode[0])
ct.set_default_color_theme("blue")


def click_func():
    percentage_complete = 0
    print("working")
    while True:
        progressbar = ct.CTkProgressBar(root)
        progressbar.pack(padx=20, pady=10)
        progressbar.set(percentage_complete)
        percentage_complete += 1


root = ct.CTk()
root.geometry("500x200")
root.title("Hulaan mo Numero")
root.resizable(False, False)

progressbar = ct.CTkProgressBar(root)
progressbar.pack(padx=20, pady=10)

button1 = ct.CTkButton(root, text="Don't Press", command="click_func")
button1.pack(padx=20, pady=10)


root.mainloop()
