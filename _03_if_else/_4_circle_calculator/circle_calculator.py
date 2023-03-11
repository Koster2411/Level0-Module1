import turtle
from tkinter import messagebox, simpledialog, Tk
import math

window = Tk()
window.withdraw()

question = simpledialog.askinteger(title=("radius"), prompt=("type a radius into this box"))
# Write a Python program that asks the user for the radius of a circle.
 # Next, ask the user if they would like to calculate the area or circumference of a circle.
goodness = simpledialog.askstring(title=('radius'), prompt=('Do you want to calculate the circumference or the area of your circle'))
# If they choose area, display the area of the circle using the radius.
if goodness == "area":
    area = math.pi*math.pow(question,2)
    messagebox.showinfo(title=("area"), message=(area))
elif goodness == "circumference":
    circum = math.pi*question*2
    messagebox.showinfo(title=("circumfrence"), message=(circum))
    # Otherwise, display the circumference of the circle using the radius.

#Area = πr^2
#Circumference = 2πr
