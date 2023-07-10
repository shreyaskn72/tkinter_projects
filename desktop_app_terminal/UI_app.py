from tkinter import *
import tkinter as tk

import sys

from IPython.utils.io import Tee
from contextlib import closing
from datetime import datetime
import traceback
import sys

#Pushing console print to log file
def logging_print_decorator(func):
    def wrapper(arg1="terminal", *args):
        terminal_log_file_name = arg1+".log"

        with closing(Tee(terminal_log_file_name, "a", channel="stdout")) as outputstream:
            try:
                func(*args)

            except Exception as e:
                print(e)

                traceback.print_exc(file=sys.stdout)


    return wrapper


@logging_print_decorator
def addNumbers():
    res = int(entry1.get()) + int(entry2.get())
    print("Inputs to be added are: ", entry1.get(), "and", entry2.get())
    print("sum is: ", res)
    print("\n")
    myText.set(res)


window = Tk()
myText = StringVar()
#getting screen width and height of display
width= window.winfo_screenwidth()
height= window.winfo_screenheight()

#setting tkinter window size
window.geometry("%dx%d" % (width/1.5, height/1.5))
Label(window, text="Number 1").grid(row=0, sticky=W)
Label(window, text="Number 2").grid(row=1, sticky=W)
Label(window, text="TOTAL:").grid(row=3, sticky=W)
total = Label(window, text="", textvariable=myText).grid(row=3, column=1, sticky=W)




entry1 = Entry(window)
entry2 = Entry(window)

entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)

button_press = Button(window, text="SUMMATION", command=addNumbers)
button_press.grid(row=0, column=2, columnspan=2, rowspan=2, sticky=W + E + N + S, padx=5, pady=5)


textwidget = tk.Text(window)

textwidget.insert(tk.END, myText)
textwidget.grid(row=4, column=3, sticky="WE")


v=Scrollbar(textwidget, orient='vertical')
v.pack(side=RIGHT, fill='y')

# Add a Scrollbar(Vertical)
h=Scrollbar(textwidget, orient='horizontal')
h.pack(side=BOTTOM, fill='x')



textbox=Text(textwidget, font=("Calibri, 16"), wrap=NONE, xscrollcommand=h.set,  yscrollcommand=v.set)

# Attach the scrollbar with the text widget
v.config(command=textbox.yview)
h.config(command=textbox.xview)
textbox.pack()

#Pushing console print to tkinter text box
def tkinter_print_decorator(func):
    def inner(inputStr):
        try:
            textbox.insert(INSERT, inputStr)
            return func(inputStr)
        except:
            return func(inputStr)
    return inner

sys.stdout.write=tkinter_print_decorator(sys.stdout.write)

mainloop()