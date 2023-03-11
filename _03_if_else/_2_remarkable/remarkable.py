from tkinter import messagebox, simpledialog, Tk
window = Tk()
window.withdraw()
question = simpledialog.askstring(title=('name'), prompt=('type in a name upper case front letter(Joe, Jill).'))
if question == "Jim":
    messagebox.showinfo(title=('Jim'), message=("Jim loves to sleep"))
elif question == "John":
    messagebox.showinfo(title=('John'), message=("John is very smart"))
elif question == "Andrew":
    messagebox.showinfo(title=('Andrew'), message=("Andrew is very tall"))
elif question == "Elliot":
    messagebox.showinfo(title=('Elliot'), message=("Elliot is good at sports"))
elif question == "Ethan":
    messagebox.showinfo(title=('Ethan'), message=("Ethan is a gardener"))
else:
    messagebox.showerror(title=('error'), message=("name not found"))
window.destroy()
