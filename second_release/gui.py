import os
from tkinter import *
import tkinter.messagebox

gui = tkinter.Tk()
gui.configure(background="purple")
gui.title("Test Case Generator")
# gui.geometry("300x180")
equation = StringVar()
expression_field = Entry(gui, textvariable=equation)
expression_field.grid(columnspan=4, ipadx=70)
equation.set('Select the type of test case:')

# Calling the generation script
def type1():
    os.system('python3 type1.py')
def type2():
    os.system('python3 type2.py')
def type3():
    os.system('python3 type3.py')
def new_format():
    os.system('python3 new_format.py')


button1 = Button(gui, text=' T\nn\nA1 A2 A3...\nn\nA1 A2 A3... ', fg='black',
                 command=type1)#, height=1, width=7)
button1.grid(row=2, column=0)
button2 = Button(gui, text=' T\nm n\nA1 A2 A3...\nm n\nA1 A2 A3... ', fg='black',
                 command=type2)#, height=1, width=7)
button2.grid(row=2, column=1)

button3 = Button(gui, text=' T\nA1 B1\nA2 B2\n. .\n. . ', fg='black',
                 command=type3, width=7)
button3.grid(row=2, column=2)

button4 = Button(gui, text=' Another type ', fg='black',
                 command=new_format)# , height=1, width=7)
button4.grid(row=3, column=1)

gui.mainloop()
