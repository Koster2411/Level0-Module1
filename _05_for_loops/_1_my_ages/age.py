from tkinter import simpledialog,messagebox,Tk


window = Tk()
window.withdraw()
Number = simpledialog.askinteger(title=("age"), prompt=("how old are you"))
for i in range(Number):
       print(str(i+1))

