from tkinter import Frame, Label, Text, INSERT, DISABLED
from lib.load import Load
from lib.link import Link
import webbrowser

conf = Load('yaml')

if conf['root']['content']['intro']['link']:
    def open_link():
        webbrowser.open_new_tab(conf['root']['content']['intro']['link'])

def Intro(target):
    frame = Frame(target)

    title = Label(frame, text='\n'+conf['root']['content']['intro']['title'], font='Helvetica 18 bold')
    description = Text(frame, borderwidth=0, highlightthickness=0, width=42, height=2)

    title.pack()
    description.pack()
    hyperlink = Link(description)

    if ':' in conf['root']['content']['intro']['description']:
        for i in conf['root']['content']['intro']['description'].split(':'):
            description.insert(INSERT, i.split('*')[0], hyperlink.add(open_link)) if '*' in i else description.insert(INSERT, i)
    else:
        description.insert(INSERT, conf['root']['content']['intro']['description'])

    description.config(state=DISABLED)

    return frame
