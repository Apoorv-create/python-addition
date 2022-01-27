#Data Type Error Project

from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("Additon")

root.geometry("600x400")

input_box = Entry(root)
input_box.pack()

def addition():
    number = 5
    get_input = input_box.get()
    try:
        print = (number + get_input)
    except(TypeError):
        messagebox.showinfo("Error!", "Can't Add Two different Variable types: Integer and String")

button = Button(root, text = "Additon", command=addition)        
button.pack()
root.mainloop()