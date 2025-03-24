from tkinter import *
import calendar

root =Tk()
root.geometry("400x400")

def cal():
    new_root= Tk()
    new_root.geometry("600x600")
    new_root.title("calender")
    fetch_year = int(e.get())
    cal_content = calendar.calendar(fetch_year)

    cal_label = Label(new_root, text = cal_content ,font = "Consolas 10 bold")
    cal_label.place(x=300,y=300)
    new_root.mainloop()


calendar = Label(root, text = "calender")
calendar.place(x =170, y =50)

ey = Label (root, text = "enter year", bg = "green")
ey.place(x=170, y=100)

e= Entry(root, width = 20)
e.place(x =150, y =150)

SC = Button(root, text = "show calendar",bg = "red", command = cal)
SC.place(x = 155, y = 200)
exit = Button(root, text = "Exit",bg = "red", command = root.destroy)
exit.place(x=175,y = 250)
root.mainloop()