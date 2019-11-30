from tkinter import Frame, Label
from lib.load import load

conf = load('yaml')

def Intro(target):
    frame = Frame(target)

    title = Label(frame, text='this is the intro section title')
    title.pack()
    description = Label(frame, text='this is the intro section description')
    description.pack()

    print(conf)

    return frame
