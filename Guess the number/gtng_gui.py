import tkinter as tk
import ttkbootstrap as ttk
from numguess import *

# import time


def guess():
    last_guess = entry_var.get()
    if is_correct(last_guess, num_to_guess):
        label_prompt_var.set(value="You are correct!")
        label_prompt_var2.set(value="")

    else:
        label_prompt_var.set(value="Try Again!")
        x = clue(last_guess, num_to_guess)
        label_prompt_var2.set(value=x)


# create window
window = ttk.Window(themename="darkly")
window.title("Guess The Number Game")
width = 500
height = 300
window.geometry(f"{width}x{height}")
window.resizable(False, False)

# create widget variables
label_prompt_var = tk.StringVar()
label_prompt_var.set(value=prompt(max_range))
label_prompt_var2 = tk.StringVar()
entry_var = tk.IntVar()

# create widgets
frame_prompt = ttk.Frame(window).pack(pady=10)
label_prompt = ttk.Label(
    frame_prompt,
    font="Calibri 18",
    textvariable=label_prompt_var,
).pack(pady=5)
label_prompt2 = ttk.Label(
    frame_prompt, font="Calibri 18", textvariable=label_prompt_var2, bootstyle="warning"
).pack(pady=5)
frame_player = ttk.Frame(window).pack(pady=10)
entry = ttk.Entry(frame_player, textvariable=entry_var).pack(pady=10)
guess_button = ttk.Button(frame_player, text="GUESS!", command=guess)
guess_button.pack(pady=10)
window.bind("<Return>", lambda event: guess())

# window mainloop()
window.mainloop()
