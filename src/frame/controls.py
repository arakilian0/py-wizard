from tkinter import *

def Controls(target):
    frame = Frame(target, bg='red')

    title = Label(frame, text='this is the controls section')
    title.pack()

    return frame
