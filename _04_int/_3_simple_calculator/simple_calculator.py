"""
* Write a Python program that asks the user for two numbers.

* Then ask the user if the would like to add, subtract, multiply, or divide.

* Use if-else statements to provide the desired math operation on the numbers
  and display the result.
"""
from tkinter import messagebox, simpledialog, Tk
window = Tk()
window.withdraw()
number1 = simpledialog.askinteger(title=("number"), prompt=("type a number into this box"))
number2 = simpledialog.askinteger(title=("number"), prompt=("type a number into this box"))
question = simpledialog.askstring(title=(""), prompt=("do you want to multiply divide subtract or add"))
if question == ("add"):
    number3 = number2 + number1
elif question == ("subtract"):
    number3 = number1 - number2
elif question == ("multiply"):
    number3 = number2 * number1
elif question == ("divide"):
    number3 = number1 / number2
messagebox.showinfo(title=("number"), message=("your numbers equal = "+str(number3)))

