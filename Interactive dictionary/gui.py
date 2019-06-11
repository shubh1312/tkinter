from tkinter import *
import app


def run_app():
    output = app.dictionary(e1_value.get())
    if type(output) == list:
        t1.delete(1.0, END)
        t1.insert(END, '\n'.join(output))
    else:
        t1.delete(1.0, END)
        t1.insert(END, *output)
# this is to get the meaning of suggested word by programm


def run_app2():
    output = app.dictionary_final(e1_value.get())
    if type(output) == list:
        t1.delete(1.0, END)
        t1.insert(END, '\n'.join(output))
    else:
        t1.delete(1.0, END)
        t1.insert(END, *output)

# this function run when no button is clicked


def next():
    t1.delete(1.0, END)
    t1.insert(END, "We didn't understand your entry!! Double check the spelling.")


window = Tk()

window.title("Welcome to Shubham's interactive dictionary")

e1_value = StringVar()
e1 = Entry(window, textvariable=e1_value, width=70)
e1.grid(padx=0, row=0, column=0)

b1 = Button(window, text="Search", command=run_app, width=10)
b1.grid(padx=0, row=0, column=3)

t1 = Text(window, height=10, width=70)
t1.grid(padx=0, row=1, column=0, columnspan=4)

b2 = Button(window, text="Yes", command=run_app2, width=10)
b2.grid(padx=0, row=2, column=0, columnspan=2)

b3 = Button(window, text="NO", command=next, width=10)
b3.grid(padx=0, row=2, column=2, columnspan=2)

window.mainloop()
