#run api1.py in background

from tkinter import *
from tkinter import messagebox

import tkinter as tk
import requests

import json

#toolbar modules
from PIL import Image, ImageTk
from tkinter import Tk, Frame, Menu, Button
from tkinter import LEFT, TOP, X, FLAT, RAISED

window = Tk()



#getting screen width and height of display
width= window.winfo_screenwidth()
height= window.winfo_screenheight()

#setting tkinter window size
window.geometry("%dx%d" % (width, height))


window.title('Frontend for apis')


# Success multigrid method
def multi_grid():
    window3 = Toplevel(window)
    window3.geometry("%dx%d" % (width / 6, height / 6))
    window3.title('Multi grid window')
    for r in range(3):
        for c in range(4):
            button_name = "button"+str(r)+str(c)
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
    #print(response)




def hello_api():
    #window1 = Tk()
    window1 = Toplevel(window)

    window1.geometry("%dx%d" % (width/2, height/2))
    window1.title('Frontend for hello api')

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
                            command=lambda:Close(window1))

    quit_button.grid(row=2, column=2, sticky="WE", padx=5, pady=2)

    quit_button2 = tk.Button(window1,
                            text="QUIT APP",
                            fg="red",
                            command=quit)

    quit_button2.grid(row=2, column=0, sticky="WE", padx=5, pady=2)

    download_button = tk.Button(window1, text="Submit request", fg="green", command=lambda:check_hello(window1, name, Name, city, City, greeting, Greeting, messages, Messages, error, Error))
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
        textwidget.grid(row=6, column=0, sticky="WE",pady=2)

        credits_label = tk.Label(window2, text="UI for summation apis by Shreyas")
        credits_label.grid(row=7, column=0, sticky="S", padx=10)




def sum_api():
    #window2 = Tk()
    window2 = Toplevel(window)

    window2.geometry("%dx%d" % (width/2, height/2))
    window2.title('Frontend for summation api')

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

    download_button = tk.Button(window2, text="Submit request", fg="green", command=lambda:check_sum(window2, number1, Number1, number2, Number2, addition, Addition, error_sum, Error_Sum))
    download_button.grid(row=2, column=1, sticky="WE", padx=5, pady=2)


first_button = tk.Button(text="Hello api", fg="Blue", command=hello_api)
first_button.grid(row=10, column=10, pady=150, sticky="W")


second_button = tk.Button(text="add numbers", fg="Blue", command=sum_api)
second_button.grid(row=10, column=10, padx=320, sticky="W")

third_button = tk.Button(text="MultiGrid", fg="Blue", command=multi_grid)
third_button.grid(row=10, column=10, padx=640, sticky="W")


quit_button = tk.Button(window,
                   text="QUIT APPLICATION",
                   fg="red",
                   command=quit)

quit_button.grid(row=11, column=10, sticky="W", padx=310)
#quit_button.grid(row=2, column=0, sticky="WE")




menubar = Menu(window)

# ManuBar 1 :

editmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='File', menu=editmenu)
editmenu.add_command(label="Cut")
editmenu.add_command(label="Copy")
editmenu.add_separator()
editmenu.add_command(label="Paste")

editmenu.add_separator()
editmenu.add_command(label="Exit", command=quit)

# ManuBar 2 :
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Programs', menu=filemenu)
filemenu.add_command(label="hello api", command=hello_api)
filemenu.add_command(label="Sum api", command=sum_api)


def about_message():
    messagebox.showinfo("About", "This is an application developed by Shreyas. It contains apis and desktop application")


def help_message():
    messagebox.showinfo("Help", "Contact Shreyas")


menubar.add_command(label="About", command=about_message)

menubar.add_command(label="help", command=help_message)

menubar.add_command(label="Quit!", command=quit)




window.config(menu=menubar)





#Toolbar implementation


#toolbar1
hello_toolbar = Frame(window, bd=1, relief=RAISED)
img = Image.open("logos/hello.png")
img = img.resize((150, 150))
eimg = ImageTk.PhotoImage(img)
hello_tool_button = tk.Button(hello_toolbar, image=eimg, relief=FLAT, command=hello_api)
hello_tool_button.image = eimg
hello_tool_button.grid(row=0, column=0)
hello_toolbar.grid(row=0, column=0)



#toolbar2
sum_toolbar = Frame(window, bd=1, relief=RAISED)
img = Image.open("logos/sum.png")
img = img.resize((150, 150))
eimg = ImageTk.PhotoImage(img)
sum_tool_button = tk.Button(sum_toolbar, image=eimg, relief=FLAT, command=sum_api)
sum_tool_button.image = eimg
sum_tool_button.grid(row=0, column=1)
sum_toolbar.grid(row=0, column=1)

#toolbar3
exit_toolbar = Frame(window, bd=1, relief=RAISED)
img = Image.open("logos/exit.png")
img = img.resize((150, 150))
eimg = ImageTk.PhotoImage(img)
exitButton = tk.Button(exit_toolbar, image=eimg, relief=FLAT, command=quit)
exitButton.image = eimg
exitButton.grid(row=0, column=2)
exit_toolbar.grid(row=0, column=2)

credits_label = tk.Label(window, text="UI for apis by Shreyas", fg="green", activebackground="green", font=('Times', '18', 'italic'))


credits_label.grid(row=15, column=10, padx=250, pady=50, sticky="W")

if __name__ == "__main__":
    window.mainloop()