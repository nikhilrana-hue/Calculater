import tkinter as tk
from tkinter import *
from tkinter import ttk

window = tk.Tk()
window.title("Calculator")
window.geometry("400x470")
window.configure(bg="#313949")

display = tk.Entry(
    window,
    font=("Times New Roman", 24, "bold"),
    bg="#8F8D8D",
    fg="#000000",
    justify="right",
    relief="flat"
)
display.place(x=20, y=20, width=350, height=70)

#function of calculator.

def click(num):
    result = display.get()
    display.delete(0,END)
    display.insert(0,str(result)+str(num))

def add():
    n1 = display.get()
    global maths
    maths = "addition"
    global i
    i = float(n1)
    display.delete(0,END)

def sub():
    n1 = display.get()
    global maths
    maths = "subtraction"
    global i
    i = float(n1)
    display.delete(0,END)

def multiply():
    n1 = display.get()
    global maths
    maths = "multipliction"
    global i
    i = float(n1)
    display.delete(0,END)

def divide():
    n1 = display.get()
    global maths
    maths = "division"
    global i
    i = float(n1)
    display.delete(0,END)

def equal():
    n2 = display.get()
    display.delete(0,END)
    if maths == "addition":
        display.insert(0, i+float(n2))
    elif maths == "subtraction":
        display.insert(0, i-float(n2))
    elif maths == "multipliction":
        display.insert(0, i*float(n2))
    elif maths == "division":
        display.insert(0, i/float(n2))

def clear():
    display.delete(0,END)

def back():
    current = display.get()
    if current:
        display.delete(len(current) - 1, END)


def point():
    current = display.get()
    if "." not in current:
        display.insert(END, ".")

def percent():
    current = display.get()
    if current:
        result = float(current) / 100
        if result == float(result):
            result = float(result)
        display.delete(0, END)
        display.insert(0, result)

#Button for all clear.
button_c = tk.Button(text="C",command=clear,font=("Times New Roman", 16, "bold"))
button_c.place(x=20,y=110,width=80,height=60)

#Button for backspace.
button_back = tk.Button(text="⌫",command=back,font=("Times New Roman", 16, "bold"))
button_back.place(x=110,y=110,width=80,height=60)

#Button for percentage.
button_percent = tk.Button(text="%", command=percent,font=("Times New Roman", 16, "bold"))
button_percent.place(x=200,y=110,width=80,height=60)

#Button for divide.
button_divide = tk.Button(text="/", command=divide,font=("Times New Roman", 16, "bold"))
button_divide.place(x=290,y=110,width=80,height=60)

#Button for multiply.
button_multiply = tk.Button(text="X", command=multiply,font=("Times New Roman", 16, "bold"))
button_multiply.place(x=290,y=180,width=80,height=60)

#Button for add.
button_add = tk.Button(text="+", command=add,font=("Times New Roman", 16, "bold"))
button_add.place(x=290,y=320,width=80,height=60)

#Button for subtract.
button_subtract = tk.Button(text="-", command=sub,font=("Times New Roman", 16, "bold"))
button_subtract.place(x=290,y=250,width=80,height=60)

#Button for point.
button_point = tk.Button(text=".", command=point,font=("Times New Roman", 16, "bold"))
button_point.place(x=200,y=390,width=80,height=60)

#Button for answer.
button_answer = tk.Button(text="=", command=equal,font=("Times New Roman", 16, "bold"))
button_answer.place(x=290,y=390,width=80,height=60)

#Button for 1.
button_1 = tk.Button(text="1", command=lambda:click(1),font=("Times New Roman", 16, "bold"))
button_1.place(x=20,y=320,width=80,height=60)

#Button for 2.
button_2 = tk.Button(text="2", command=lambda:click(2),font=("Times New Roman", 16, "bold"))
button_2.place(x=110,y=320,width=80,height=60)

#Button for 3.
button_3 = tk.Button(text="3", command=lambda:click(3),font=("Times New Roman", 16, "bold"))
button_3.place(x=200,y=320,width=80,height=60)

#Button for 4.
button_4 = tk.Button(text="4", command=lambda:click(4),font=("Times New Roman", 16, "bold"))
button_4.place(x=20,y=250,width=80,height=60)

#Button for 5.
button_5 = tk.Button(text="5", command=lambda:click(5),font=("Times New Roman", 16, "bold"))
button_5.place(x=110,y=250,width=80,height=60)

#Button for 6.
button_6 = tk.Button(text="6", command=lambda:click(6),font=("Times New Roman", 16, "bold"))
button_6.place(x=200,y=250,width=80,height=60)

#Button for 7.
button_7 = tk.Button(text="7", command=lambda:click(7),font=("Times New Roman", 16, "bold"))
button_7.place(x=20,y=180,width=80,height=60)

#Button for 8.
button_8 = tk.Button(text="8", command=lambda:click(8),font=("Times New Roman", 16, "bold"))
button_8.place(x=110,y=180,width=80,height=60)

#Button for 9.
button_9 = tk.Button(text="9", command=lambda:click(9),font=("Times New Roman", 16, "bold"))
button_9.place(x=200,y=180,width=80,height=60)

#Button for 0.
button_0 = tk.Button(text="0", command=lambda:click(0),font=("Times New Roman", 16, "bold"))
button_0.place(x=20,y=390,width=170,height=60)

window.mainloop()