from tkinter import *
from random import randint as rnd

def change_loc():
    button.place(x = rnd(0,400), y = rnd(0, 400), width = rnd(50, 100), height = rnd(50, 100))
    button['text'] += 1

window = Tk()
window.geometry('500x500')
button = Button(window, text = 0, command = change_loc)
button.place(x = rnd(0,400), y = rnd(0, 400), width = rnd(50, 100), height = rnd(50, 100))

window.mainloop()