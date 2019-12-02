from tkinter import *
from lib import Config, Link
import webbrowser

conf = Config()

def link_click():
    webbrowser.open_new_tab('https://google.com')

# Intro Frame
def Intro(target):
    frame = Frame(target)

    intro_description = Text(frame, borderwidth=0, highlightthickness=0, width=56, height=2)
    intro_description.pack()
    hyperlink = Link(intro_description)
    intro_description.insert(INSERT, 'Installs the ')
    intro_description.insert(INSERT, 'about-me', hyperlink.add(link_click))
    intro_description.insert(INSERT, ' executable and configures path.')
    intro_description.insert(INSERT, '')
    intro_description.config(state=DISABLED)
    # hyperlink = Link(title)

    # title.insert(INSERT, 'asd')
    # title.insert(INSERT, 'asd')
    # title.insert(INSERT, 'asd')

    return frame

# Path Frame
def Path(target):
    frame = Frame(target)

    intro_description = Text(frame, borderwidth=0, highlightthickness=0, width=56, height=2)
    intro_description.pack()
    hyperlink = Link(intro_description)
    intro_description.insert(INSERT, 'Installs the ')
    intro_description.insert(INSERT, 'about-me', hyperlink.add(link_click))
    intro_description.insert(INSERT, ' executable and configures path.')
    intro_description.insert(INSERT, '')
    intro_description.config(state=DISABLED)
    # hyperlink = Link(title)

    # title.insert(INSERT, 'asd')
    # title.insert(INSERT, 'asd')
    # title.insert(INSERT, 'asd')

    return frame

# License Frame
def License(target):
    frame = Frame(target)

    intro_description = Text(frame, borderwidth=0, highlightthickness=0, width=56, height=2)
    intro_description.pack()
    hyperlink = Link(intro_description)
    intro_description.insert(INSERT, 'Installs the ')
    intro_description.insert(INSERT, 'about-me', hyperlink.add(link_click))
    intro_description.insert(INSERT, ' executable and configures path.')
    intro_description.insert(INSERT, '')
    intro_description.config(state=DISABLED)
    # hyperlink = Link(title)

    # title.insert(INSERT, 'asd')
    # title.insert(INSERT, 'asd')
    # title.insert(INSERT, 'asd')

    return frame

# Control Frame
def Control(target):
    frame = Frame(target)

    intro_description = Text(frame, borderwidth=0, highlightthickness=0, width=56, height=2)
    intro_description.pack()
    hyperlink = Link(intro_description)
    intro_description.insert(INSERT, 'Installs the ')
    intro_description.insert(INSERT, 'about-me', hyperlink.add(link_click))
    intro_description.insert(INSERT, ' executable and configures path.')
    intro_description.insert(INSERT, '')
    intro_description.config(state=DISABLED)
    # hyperlink = Link(title)

    # title.insert(INSERT, 'asd')
    # title.insert(INSERT, 'asd')
    # title.insert(INSERT, 'asd')

    return frame
