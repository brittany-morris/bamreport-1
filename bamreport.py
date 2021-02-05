#!/usr/bin/env python3

from tkinter import *

#create a blank window called root
root = Tk()
root.title('Bam Reporting')

#set the size
root.geometry('1000x1000')

#create a label widget
#put it on a grid to determine where the label lies on the window
lbl = Label(root, text = "Welcome To Bam Reporting")
lbl.grid(column = 0, row = 0)

#creating a dropdown menu
def show():
    lbl2 = Label(root, text=clicked.get()).grid(column = 0, row = 3)

clicked = StringVar()
clicked.set("Select Options")

options1 = [
        "options",
        "for",
        "dropdown",
        "menu"
]

drop = OptionMenu(root, clicked, *options1)
drop.grid(column = 0, row = 1)

#need to fix issue where if user clicks button, the option selected will print over the last
myButton = Button(root, text = "show selection", command = show).grid(column = 0, row = 4)

#creating a dropdown menu
def show():
    lbl2 = Label(root, text=clicked.get()).grid(column = 1, row = 3)

clicked = StringVar()
clicked.set("Select Options")

options1 = [
        "options",
        "for",
        "dropdown",
        "menu"
]

drop = OptionMenu(root, clicked, *options1)
drop.grid(column = 1, row = 1)

#need to fix issue where is user cclicks button, the option will print over the last
myButton = Button(root, text = "show selection", command = show).grid(column = 1, row = 4)

#creating a dropdown menu
def show():
    lbl2 = Label(root, text=clicked.get()).grid(column = 2, row = 3)

clicked = StringVar()
clicked.set("Select Options")

options1 = [
        "options",
        "for",
        "dropdown",
        "menu"
]

drop = OptionMenu(root, clicked, *options1)
drop.grid(column = 2, row = 1)

#need to fix issue where if user clicks button, the option selected will print over the las
myButton = Button(root, text = "show selection", command = show).grid(column = 2, row = 4)

#call the mainloop funtion to run the program
root.mainloop()
