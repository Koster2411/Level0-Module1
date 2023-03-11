from tkinter import messagebox, simpledialog
import tkinter as tk
window_width = 600
window_height = 600

root = tk.Tk()

canvas = tk.Canvas(root, width=window_width, height=window_height, bg="#DDDDDD")
canvas.grid()

# 1. Ask the user what color tomato they would like and save their response
message = simpledialog.askstring(title=("what tomato"), prompt=("type in either red, green or yellow"))
#    You can give them up to three choices


# 2. Use if-else statements to draw the tomato in the color that they chose
if message == "red":
    canvas.create_oval(75, 200, 400, 450, fill="red", outline="")
    canvas.create_oval(200, 200, 525, 450, fill="red", outline="")
    canvas.create_rectangle(275, 100, 325, 230, fill="green", outline="")
elif message == "green":
    canvas.create_oval(75, 200, 400, 450, fill="green", outline="")
    canvas.create_oval(200, 200, 525, 450, fill="green", outline="")
    canvas.create_rectangle(275, 100, 325, 230, fill="green", outline="")
elif message == "yellow":
    canvas.create_oval(75, 200, 400, 450, fill="yellow", outline="")
    canvas.create_oval(200, 200, 525, 450, fill="yellow", outline="")
    canvas.create_rectangle(275, 100, 325, 230, fill="green", outline="")
else:
    canvas.create_oval(75, 200, 400, 450, fill="black", outline="")
    canvas.create_oval(200, 200, 525, 450, fill="black", outline="")
    canvas.create_rectangle(275, 100, 325, 230, fill="green", outline="")
    messagebox.showerror(title=("rotten"), message=("you get a rotten tomato"))

#canvas.create_rectangle(275, 100, 325, 230, fill="green", outline="")

root.mainloop()
