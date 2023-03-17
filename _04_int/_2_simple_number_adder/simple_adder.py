
from tkinter import messagebox, simpledialog, Tk
window = Tk()
window.withdraw()
number1 = simpledialog.askinteger(title=("number"), prompt=("type a number into this box"))
number2 = simpledialog.askinteger(title=("number"), prompt=("type a number into this box"))
number3 = number2 + number1
messagebox.showinfo(title=("number"), message=("your numbers equal = "+str(number3)))


