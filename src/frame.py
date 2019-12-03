from tkinter import *
from lib import *

conf = config()

# Intro Frame
#########################################################################
def Intro(target):
    _title = conf['root']['content']['intro']['title']
    _description = conf['root']['content']['intro']['description']
    frame = Frame(target)
    whitespace = Label(frame, text='').pack()
    title = Label( frame ,
                text=_title['entry'],
                width=_title['width'],
                height=_title['height'],
                fg=_title['color'],
                font=Font(_title['font'])
            )
    description = Text( frame ,
                width=_description['width'],
                height=_description['height'],
                fg=_description['color'],
                font=Font(_description['font'])
            )
    title.pack()
    description.pack()
    hyperlink = Link(description)

    if ':' in _description['entry']:
        for i in _description['entry'].split(':'):
            if '*' in i:
                description.insert( INSERT ,
                    i.split('*')[0],
                    hyperlink.add(OpenLink)
                )
            else:
                description.insert(INSERT, i)

    description.config(state=DISABLED)
    return frame

# Path Frame
#########################################################################
def Path(target):
    _input = conf['root']['content']['path']['input']
    _button = conf['root']['content']['path']['button']
    frame = Frame(target)
    whitespace = Label(frame, text='').pack()
    input = Label( frame ,
                text=SetPath(),
                fg=_input['color'],
                width=_input['width'],
                height=_input['height'],
                borderwidth=_input['borderwidth'],
                relief=_input['relief'],
                font=Font(_input['font'])
            )
    button = Label( frame ,
                text=_button['entry'],
                fg=_button['color'],
                bg=_button['background'],
                width=_button['width'],
                height=_button['height'],
                font=Font(_button['font'])
            )
    input.pack(side=LEFT)
    button.bind('<Button-1>', ChangePath)
    button.pack(side=RIGHT)

    return frame

# License Frame
#########################################################################
def License(target):
    frame = Frame(target)
    whitespace = Label(frame, text='').pack()

    demo = Label(frame, text="some text")
    demo.pack()

    return frame

# Control Frame
#########################################################################
def Control(target):
    _quit = conf['root']['content']['control']['quit']
    _install = conf['root']['content']['control']['install']
    _seperator = conf['root']['content']['control']['seperator']

    frame = Frame(target)
    whitespace = Label(frame).pack()
    seperator = Label(frame, width=_seperator['width'])
    quit = Label( frame ,
                        text=_quit['entry'],
                        fg=_quit['color'],
                        bg=_quit['background'],
                        width=_quit['width'],
                        height=_quit['height'],
                        font=Font(_quit['font'])
                    )
    install = Label( frame ,
                        text=_install['entry'],
                        fg=_install['color'],
                        bg=_install['background'],
                        width=_install['width'],
                        height=_install['height'],
                        font=Font(_install['font'])
                    )
    quit.bind("<Button-1>", Quit)
    install.bind("<Button-1>", Install)

    quit.pack(side=LEFT)
    seperator.pack(side=LEFT)
    install.pack(side=RIGHT)

    return frame
