#!/usr/bin/env python3

from tkinter import *
from tkcalendar import * 

#create a blank window called root
root = Tk()
root.title('Bam Reporting')

#set the size
root.geometry('1000x1000')

#create a label widget
#put it on a grid to determine where the label lies on the window
lbl = Label(root, text = "Welcome To Bam Reporting")
lbl.grid(column = 0, row = 0)



#making a date entry widget

select_date_lbl = Label(root, text = "Please select the date").grid(column = 0, row = 1) 

cal = Calendar(root, selectmode = "day", year = 2021, month = 2, day = 5)
cal.grid(column = 0 , row = 2)

def grab_date():
    cal_label.config(text = cal.get_date())

cal_button = Button(root, text = "Get Date", command = grab_date)
cal_button.grid(column = 0, row = 3)

cal_label = Label(root, text = "")
cal_label.grid(column = 0, row = 4)



#creating a dropdown menu
def show():
    lbl2 = Label(root, text=clicked1.get()).grid(column = 1, row = 3)

clicked1 = StringVar()
clicked1.set("Select Options")

options1 = [
        "options",
        "for",
        "dropdown",
        "menu"
]

drop = OptionMenu(root, clicked1, *options1)
drop.grid(column = 1, row = 1)

#need to fix issue where if user clicks button, the option selected will print over the last
myButton = Button(root, text = "show selection", command = show).grid(column = 1, row = 2)



#creating a dropdown menu
def show():
    lbl3 = Label(root, text=clicked2.get()).grid(column = 2, row = 3)

clicked2 = StringVar()
clicked2.set("Select Options")

options2 = [
        "options",
        "for",
        "dropdown",
        "menu"
]

drop = OptionMenu(root, clicked2, *options2)
drop.grid(column = 2, row = 1)

#need to fix issue where is user cclicks button, the option will print over the last
myButton = Button(root, text = "show selection", command = show).grid(column = 2, row = 2)



#creating a dropdown menu
def show():
    lbl4 = Label(root, text=clicked3.get()).grid(column = 3, row = 3)

clicked3 = StringVar()
clicked3.set("Select Options")

options3 = [
        "options",
        "for",
        "dropdown",
        "menu"
]

drop = OptionMenu(root, clicked3, *options3)
drop.grid(column = 3, row = 1)

#need to fix issue where if user clicks button, the option selected will print over the las
myButton = Button(root, text = "show selection", command = show).grid(column = 3, row = 2)

#call the mainloop funtion to run the program
root.mainloop()
