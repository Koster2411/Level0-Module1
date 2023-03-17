"""
* Write a python program that asks the user a minimum of 3 riddles.

* You can look at riddles.com if you don't already know any riddles.

* Collect the response of each riddle from the user and compare their
  answers to the correct answer.

* Use a variable to keep track of the correctly answered riddles

* After all the riddles have been asked, tell the user how many they got
  correct
"""
#
from tkinter import messagebox, simpledialog, Tk
score = 0
window = Tk()
window.withdraw()
riddle1 = simpledialog.askstring(title=("riddle"), prompt=("What belongs to you, but other people use it more than you?"))

if riddle1 == ("Your name"):
    score = score + 1
riddle2 = simpledialog.askstring(title=("riddle"), prompt=(" How many sides does a circle have?"))
if riddle2 == ("2,The outside and the inside"):
    score = score + 1

riddle3 = simpledialog.askstring(title=("riddle"), prompt=("Why is Europe like a frying pan?"))
if riddle3 == ("Because it has Greece at the bottom"):
    score += 1
messagebox.showinfo(title=("score"), message=("you got"+str(score)))

