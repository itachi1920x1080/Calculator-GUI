from tkinter import PhotoImage
from tkinter import Button
import tkinter as tk
from math import *


def button_click(item):
    current = display_var.get()
    if current == "0" and str(item) != ".":
        display_var.set(str(item))
    elif current == "Error":
        display_var.set(str(item))
    else: 
        display_var.set(current + str(item)) 

def button_clear():
    display_var.set("0")
def button_clear_entry():
    current = display_var.get()
    if current:
        if current == "Error" or len(current)==1:
            display_var.set("0")
        else:   
            display_var.set(current[:-1])
    else :
        display_var.set("0")
def button_delete():
    current = display_var.get()
    if current == "0" or current == "Error":
        display_var.set("")
    else:   
        display_var.set(current[:-1])
def button_equals():
    try:
        result = eval(display_var.get())
        display_var.set(result)
    except: 
        display_var.set("Error")

root =tk.Tk()
root.title(" Python Calculator")
root.geometry("360x499")
root.resizable(0,0)
icon_image = tk.PhotoImage(file="assets/my_logo.png")
root.iconphoto(False, icon_image)

display_var =tk.StringVar()
display_var.set(0) 
display = tk.Entry(root,textvariable=display_var,font=('Arial',20,'bold'),bg='#eee',bd=10,justify="right")
display.grid(row=0,column=0,columnspan=4,ipady=20,pady=10)

button = [
    ('7',1,0),('8',1,1),('9',1,2),('/',1,3),
    ('4',2,0),('5',2,1),('6',2,2),('*',2,3),
    ('1',3,0),('2',3,1),('3',3,2),('-',3,3),
    ('0',4,0),('.',4,1),('=',4,2),('+',4,3),
    ('CE',5,0),('C',5,1),('DEL',5,2)        
]


for (text , row ,col)in button:
    if text == '=':
        btn = tk.Button(root, text=text, font=('Arial', 18, 'bold'), bg="#4caf50", fg="white",command=button_equals,height=2, width=5)
    elif text == 'C':
        btn = tk.Button(root, text=text, font=('Arial', 18, 'bold'), bg="#4caf50", fg="white", command=button_clear, height=2, width=5)
    elif text == 'CE':
        btn = tk.Button(root, text=text, font=('Arial', 18, 'bold'), bg="#4caf50", fg="white", command=button_clear_entry, height=2, width=5)
    elif text == 'DEL':
        btn = tk.Button(root, text=text, font=('Arial', 18, 'bold'), bg="#4caf50", fg="white", command=button_delete, height=2, width=5)
    else:
        btn = tk.Button(root, text=text, font=('Arial', 18, 'bold'), bg="#fff",
                        command=lambda t=text: button_click(t), height=2, width=5)
    btn.grid(row=row,column=col,sticky="nsew")
root.mainloop()