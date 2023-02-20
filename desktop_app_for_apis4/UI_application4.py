# run api1.py in background

from tkinter import *
from tkinter import messagebox

import tkinter as tk
import requests

import json

# toolbar modules
from PIL import Image, ImageTk
from tkinter import Tk, Frame, Menu, Button
from tkinter import LEFT, TOP, X, FLAT, RAISED

window = Tk()

# getting screen width and height of display
width = window.winfo_screenwidth()
height = window.winfo_screenheight()

# setting tkinter window size
window.geometry("%dx%d" % (width, height))

window.title('Frontend for apis')


# color of the window
# window.config(bg='cyan')


# Success multigrid method
def multi_grid():
    window3 = Toplevel(window)
    window3.geometry("%dx%d" % (width / 6, height / 6))
    window3.title('Multi grid window')
    for r in range(3):
        for c in range(4):
            button_name = "button" + str(r) + str(c)
            button_name = tk.Button(window3, fg="Red", text='B%s%s' % (r, c), borderwidth=1)
            button_name.grid(row=r, column=c, padx=r, pady=c, sticky="S")
    window3.mainloop()


def check_hello(window1, name, Name, city, City, greeting, Greeting, messages, Messages, error, Error):
    a = Name.get()
    b = City.get()
    print(a)
    print(b)

    data = {}
    data['Name'] = a
    data['City'] = b

    try:
        response = requests.post("http://127.0.0.1:5000/Hello", json=data)
        text_response = response.text

        print(response.status_code)

        if response.status_code == 200:

            dict_response = json.loads(text_response)

            error.grid(row=3, column=0)
            Error.grid(row=3, column=1)

            greeting.grid(row=4, column=0)
            messages.grid(row=5, column=0)

            # role.grid(row=2, column=0)
            Greeting.grid(row=4, column=1)
            Messages.grid(row=5, column=1)

            Error.delete(0, tk.END)
            Error.insert(0, "None")

            Greeting.delete(0, tk.END)
            Greeting.insert(0, dict_response["Greeting"])

            Messages.delete(0, tk.END)
            Messages.insert(0, dict_response["Message"])

            textwidget = tk.Text(window1)
            textwidget.insert(tk.END, text_response)
            textwidget.grid(row=6, column=0, sticky="WE", padx=5, pady=2)
            credits_label = tk.Label(window1, text="UI for hello api by Shreyas")
            credits_label.grid(row=7, column=0, sticky="S", padx=2)

        else:

            error.grid(row=3, column=0)
            Error.grid(row=3, column=1)
            Error.delete(0, tk.END)
            Error.insert(tk.END, text_response)

            greeting.grid(row=4, column=0)
            messages.grid(row=5, column=0)

            # role.grid(row=2, column=0)
            Greeting.grid(row=4, column=1)
            Messages.grid(row=5, column=1)

            Greeting.delete(0, tk.END)
            Greeting.insert(0, "N/A")

            Messages.delete(0, tk.END)
            Messages.insert(0, "N/A")

            # textwidget = tk.Text()
            textwidget = tk.Text(window1)
            textwidget.insert(tk.END, text_response)
            textwidget.grid(row=6, column=0, sticky="WE", padx=2)
            credits_label = tk.Label(window1, text="UI for hello api by Shreyas")
            credits_label.grid(row=7, column=0, sticky="S", padx=10)






    except Exception as e:

        print(e)
        text_response = e

        error.grid(row=3, column=0)
        Error.grid(row=3, column=1)
        Error.insert(tk.END, e)

        greeting.grid(row=4, column=0)
        messages.grid(row=5, column=0)

        # role.grid(row=2, column=0)
        Greeting.grid(row=4, column=1)
        Messages.grid(row=5, column=1)

        Greeting.delete(0, tk.END)
        Greeting.insert(0, "N/A")

        Messages.delete(0, tk.END)
        Messages.insert(0, "N/A")

        # textwidget = tk.Text()
        textwidget = tk.Text(window1)
        textwidget.insert(tk.END, text_response)
        textwidget.grid(row=6, column=0, sticky="WE", padx=5, pady=2)

        credits_label = tk.Label(window1, text="UI for hello api by Shreyas")
        credits_label.grid(row=7, column=0, sticky="S", padx=10)

    # Role.grid(row=2, column=1)
    # print(response)


def hello_api():
    # window1 = Tk()
    window1 = Toplevel(window)

    window1.geometry("%dx%d" % (width / 2, height / 2))
    window1.title('Frontend for hello api')

    window1.attributes("-topmost", True)  # Put this window in foreground

    name = Label(window1, text="Name:")
    Name = Entry(window1)
    city = Label(window1, text="City:")
    City = Entry(window1)

    greeting = Label(window1, text="Greeting:")
    Greeting = Entry(window1)
    messages = Label(window1, text="Message:")
    Messages = Entry(window1)

    error = Label(window1, text="Error:")
    Error = Entry(window1)

    def Close(root):
        root.destroy()

    name.grid(row=0, column=0)
    city.grid(row=1, column=0)

    Name.grid(row=0, column=1)
    City.grid(row=1, column=1)

    quit_button = tk.Button(window1,
                            text="QUIT hello",
                            fg="orange",
                            command=lambda: Close(window1))

    quit_button.grid(row=2, column=2, sticky="WE", padx=5, pady=2)

    quit_button2 = tk.Button(window1,
                             text="QUIT APP",
                             fg="red",
                             command=quit)

    quit_button2.grid(row=2, column=0, sticky="WE", padx=5, pady=2)

    download_button = tk.Button(window1, text="Submit request", fg="green",
                                command=lambda: check_hello(window1, name, Name, city, City, greeting, Greeting,
                                                            messages, Messages, error, Error))
    download_button.grid(row=2, column=1, sticky="WE", padx=5, pady=2)


def check_sum(window2, number1, Number1, number2, Number2, addition, Addition, error_sum, Error_Sum):
    a = Number1.get()
    b = Number2.get()
    print(a)
    print(b)

    data = {}

    try:
        data['Number1'] = float(a)
        data['Number2'] = float(b)
        response = requests.post("http://127.0.0.1:5000/add", json=data)
        text_response = response.text

        print(response.status_code)

        if response.status_code == 200:

            dict_response = json.loads(text_response)
            print(dict_response)

            error_sum.grid(row=3, column=0)
            Error_Sum.grid(row=3, column=1)

            addition.grid(row=4, column=0)

            # role.grid(row=2, column=0)
            Addition.grid(row=4, column=1)

            Error_Sum.delete(0, tk.END)
            Error_Sum.insert(0, "None")

            Addition.delete(0, tk.END)
            Addition.insert(0, dict_response["sum"])

            textwidget = tk.Text(window2)
            textwidget.insert(tk.END, text_response)
            textwidget.grid(row=6, column=0, sticky="WE", pady=2)
            credits_label = tk.Label(window2, text="UI for summation apis by Shreyas")
            credits_label.grid(row=7, column=0, sticky="S", padx=10)

        else:

            error_sum.grid(row=3, column=0)
            Error_Sum.grid(row=3, column=1)
            Error_Sum.delete(0, tk.END)
            Error_Sum.insert(tk.END, text_response)

            addition.grid(row=4, column=0)

            # role.grid(row=2, column=0)
            Addition.grid(row=4, column=1)

            Addition.delete(0, tk.END)
            Addition.insert(0, "N/A")

            textwidget = tk.Text(window2)
            textwidget.insert(tk.END, text_response)
            textwidget.grid(row=6, column=0, sticky="WE", pady=2)
            credits_label = tk.Label(window2, text="UI for summation apis by Shreyas")
            credits_label.grid(row=7, column=0, sticky="S", padx=10)






    except Exception as e:

        print(e)
        text_response = e

        error_sum.grid(row=3, column=0)
        Error_Sum.grid(row=3, column=1)
        Error_Sum.insert(tk.END, e)

        addition.grid(row=4, column=0)

        # role.grid(row=2, column=0)
        Addition.grid(row=4, column=1)

        Addition.delete(0, tk.END)
        Addition.insert(0, "N/A")

        textwidget = tk.Text(window2)
        textwidget.insert(tk.END, text_response)
        textwidget.grid(row=6, column=0, sticky="WE", pady=2)

        credits_label = tk.Label(window2, text="UI for summation apis by Shreyas")
        credits_label.grid(row=7, column=0, sticky="S", padx=10)


def sum_api():
    # window2 = Tk()
    window2 = Toplevel(window)

    window2.geometry("%dx%d" % (width / 2, height / 2))
    window2.title('Frontend for summation api')

    window2.attributes("-topmost", True)  # Put this window in foreground

    number1 = Label(window2, text="Number1:")
    Number1 = Entry(window2)
    number2 = Label(window2, text="Number2:")
    Number2 = Entry(window2)

    addition = Label(window2, text="Sum:")
    Addition = Entry(window2)

    error_sum = Label(window2, text="Error:")
    Error_Sum = Entry(window2)

    def Close(root):
        root.destroy()

    number1.grid(row=0, column=0)
    number2.grid(row=1, column=0)

    Number1.grid(row=0, column=1)
    Number2.grid(row=1, column=1)

    quit_button = tk.Button(window2,
                            text="QUIT addition",
                            fg="orange",
                            command=lambda: Close(window2))

    quit_button.grid(row=2, column=2, sticky="WE", padx=5, pady=2)

    quit_button2 = tk.Button(window2,
                             text="QUIT APP",
                             fg="red",
                             command=quit)

    quit_button2.grid(row=2, column=0, sticky="WE", padx=5, pady=2)

    download_button = tk.Button(window2, text="Submit request", fg="green",
                                command=lambda: check_sum(window2, number1, Number1, number2, Number2, addition,
                                                          Addition, error_sum, Error_Sum))
    download_button.grid(row=2, column=1, sticky="WE", padx=5, pady=2)


def about_message():
    messagebox.showinfo("About", "This is an application developed by Shreyas. It contains apis and desktop application")

def help_message():
    messagebox.showinfo("Help", "Contact Shreyas")


from tkinter import filedialog


def upload_file():
    file = filedialog.askopenfilename()
    fob = open(file, 'r')
    print(fob.read())
    # file = filedialog.askopenfile()
    # print(file.read())




# Change the label text
def dispay():
    print(clicked.get())
    if clicked.get() == "hello api" :
        hello_api()

    elif clicked.get() == "Sum api":
        sum_api()

    elif clicked.get() == "multigrid":
        multi_grid()

    elif clicked.get() == "upload":
        upload_file()

    elif clicked.get() == "About":
        about_message()

    elif clicked.get() == "help":
        help_message()

    elif clicked.get() == "Quit!":
        quit()

    #label.config( text = clicked.get() )

# Dropdown menu options
options = [
	"hello api",
	"Sum api",
	"multigrid",
	"About",
	"help",
    #"upload",
	"Quit!"
]

# datatype of menu text
clicked = StringVar()

# initial menu text
clicked.set( "hello api" )

# Create Dropdown menu
drop = OptionMenu( window , clicked , *options )
drop.pack()

# Create button, it will change label text
button = Button( window , text = "Tap me" , command = dispay ).pack()

# Create Label
label = Label( window , text = " " )
label.pack()

if __name__ == "__main__":
    window.mainloop()