
import datetime


window = Tk()
window.withdraw()
birthday = simpledialog.askstring(title=("birthday"), prompt=("type in your birthday, month first and then day(d/m/yy)"))
if birthday == "3/8/20":
    messagebox.showinfo(title=("birthday"), message=("happy birthday!!!"))

else:
    messagebox.showinfo(title=("unbirthday"), message=("happy unbirthday!!"))
