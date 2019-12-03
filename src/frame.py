from tkinter import *
from lib import *

conf = Config()

# Intro Frame
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
                    hyperlink.add(Openlink0)
                )
            else:
                description.insert(INSERT, i)

    description.config(state=DISABLED)
    return frame

# Path Frame
def Path(target):
    _input = conf['root']['content']['path']['input']
    _button = conf['root']['content']['path']['button']
    frame = Frame(target)
    whitespace = Label(frame, text='').pack()
    input = Label( frame ,
                # use function to set
                # text based on
                # operating system
                text='asdsdsdsd',
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
    input.pack(side=LEFT)  # create Path Changer Function
    button.bind('<Button-1>', Openlink1)
    button.pack(side=RIGHT)
    return frame
