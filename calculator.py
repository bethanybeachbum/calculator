from ast import Lambda
from tkinter import *

# All use of TKinter starts with this command
root = Tk()
root.title("Mark's Calculator")

# Data Entry Widget
e = Entry(root, width=35, bg="#b6d7a8", fg="blue", borderwidth=5 )
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


root.configure(bg="#6aa84f")  # bg="#6aa84f"
# e.insert(0, "Enter Your To Do")

# TKinter is always a two step process: "define" and "put on screen" 
#  TKinter uses a grid system of rows and columns


# Define buttons
def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_clear():  
    e.delete(0, END)

def button_add():
    first_number = e.get()
    global f_num
    f_num = int(first_number)
    e.delete(0,END)

def button_equal():
    second_number = e.get()
    e.delete(0, END)
    e.insert(0, f_num + int(second_number))

def demoColorChange(): 
    button_1.configure(bg="red", fg="yellow")

# DEFINE BUTTONS
button_1 = Button(root, text="1", padx=38, pady=14, font=("Arial Bold", 24), command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=38, pady=14, font=("Arial Bold", 24), command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=38, pady=14, font=("Arial Bold", 24), command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=38, pady=14, font=("Arial Bold", 24), command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=38, pady=14, font=("Arial Bold", 24), command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=38, pady=14, font=("Arial Bold", 24), command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=38, pady=14, font=("Arial Bold", 24), command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=38, pady=14, font=("Arial Bold", 24), command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=38, pady=14, font=("Arial Bold", 24), command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=38, pady=14, font=("Arial Bold", 24), command=lambda: button_click(0))
button_addit = Button(root, text="+", padx=38, pady=14, font=("Arial Bold", 24), command=button_add)
# padx=102, pady=20
button_equal = Button(root, text="=", padx=102, pady=20, command=button_equal)
button_clear = Button(root, text="Clear", padx=91, pady=20, command=button_clear)

# Put buttons on screen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan=2)
button_addit.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)

root.mainloop()

# put on screen:  Shove it on screen anywhere use:
# myLabel1.pack()
