"""
* 1. Look at the image bananasplit.png

* 2. Your mission is to create a python program that recreates that image
     using the create_text function
     
* positioning so that you can read all four
     separate lines.
"""

from tkinter import *
import tkinter as tk

root = tk.Tk()

canvas = tk.Canvas(root, width=200, height=200, bg="#FF00FF");
canvas.grid()


#Text Rendering Example:
                    #x    y


# Put your code below
canvas.create_text(100, 50, text="ice cream", font=("Arial", 16))
canvas.create_text(100, 70, text="ice cream", font=("Arial", 16))
canvas.create_text(100, 90, text="ice cream", font=("Arial", 16))
canvas.create_text(100, 110, text="banana", font=("Arial", 16))
root.mainloop()
