import tkinter as tk

root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.destroy()
print("Screen resolution: {}x{}".format(screen_width, screen_height))
