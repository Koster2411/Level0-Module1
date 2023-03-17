import turtle
from tkinter import messagebox, simpledialog, Tk

# Goal: Write a Python program that asks the user whether they want to
#       draw a triangle, square, or circle and then draw that shape.

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    
    # Make a new turtle
    I = turtle.Turtle()
    
    # Ask the user what shape they want to draw and store it in a variable
    shape = simpledialog.askstring(title=("shape"), prompt=("type triangle, square, or circle into this box."))
    # Draw the shape requested by the user using if-elif-else statements
    if shape == ("square"):
        for i in range(4):
            I.forward(90)
            I.right(90)
        I.hideturtle()
        turtle.done()
    elif shape == ("triangle"):
        for i in range(3):
            I.forward(100)
            I.right(120)
        I.hideturtle()
        turtle.done()
    elif shape == ("circle"):
            I.circle(100)
            I.hideturtle()
            turtle.done()

    else:
        I.speed(0)
        for i in range(400):
            I.circle(100)

            for g in range(4):
                I.forward(100)
                I.right(i-30+20)

            for t in range(3):
                I.forward(100)
                I.right(i*2)
        I.hideturtle()
        turtle.done()




    
    # Call the turtle .done() method
