import turtle
from tkinter import messagebox, simpledialog, Tk
import math

# Goal: Write a Python program that asks the user for the radius 
#       of a circle and displays the area of that circle.
#       The formula for the area of a circle is πr^2.
#       See example image in package to check your output.

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    
    # Ask the user for the radius in pixels and store it in a variable
    radius = simpledialog.askinteger(title=("Radius"), prompt=("type a radius into this box"))
    # simpledialog.askinteger()
    
    # Make a new turtle
    turtle_ = turtle.Turtle()
    # Have your turtle draw a circle with the correct radius
    turtle_.circle(radius)

    # Call the turtle .penup() method
    turtle_.penup()
    # Move your turtle to a new x,y position using .goto()
    turtle_.goto(0, -60)
    # Calculate the area of your circle and store it in a variable
    # Hint, you can use math.pi
    area = math.pi*math.pow(radius,2)
    # Write the area of your circle using the turtle .write() method
    turtle_.write(arg="area = " + str(area), move=True, align='left', font=('Arial',20,'normal'))

    # Hide your turtle
    turtle_.hideturtle()
    # Call turtle.done()
    turtle.done()
