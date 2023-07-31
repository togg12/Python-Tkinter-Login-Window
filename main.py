import tkinter as tk
from tkinter import *
import os

# lernen von tkinter und arbeit an meinem 1 tkinter projekt = ca. 3-4st

root = tk.Tk()
root.configure(bg = "#A8A3A2")

name = "Hans"
password = "Test"

def login():
    if my_name.get() == name and my_pas.get() == password:
        print("Welcome")
        os.startfile("Moonlight.py")


root.title("Login")
root.maxsize(300, 300)
root.minsize(300, 300)

label1 = Label(root, text="Login", bg = "#A8A3A2")
label1.pack()

my_name = Entry(root, width = 20, bg = "#C4BEBC")
my_name.insert(1,"Username")
my_name.pack(padx = 5, pady = 5)

my_pas = Entry(root, width = 20)
my_pas = Entry(root, show="*", bg = "#C4BEBC")
my_pas.insert(0, "Password")
my_pas.pack(padx = 5, pady = 5)

button1 = Button(root, text = "Login", command = login, bg = "#C4BEBC")
button1.pack(pady = 3)


root.mainloop()