# Import GUI Library (Tkinter)
from tkinter import Tk

# Import Built GUI Frames
from frame.intro import Intro
from frame.path import Path
from frame.license import License
from frame.controls import Controls

# Import Utility Scripts
from lib.load import Load

# Returns 'config.yml' as Python Dictionary
conf = Load('yaml')

# Instantiate and Configure Window (root)
root = Tk()
root.title(conf['root']['window']['title'])
root.config(menu=Load('menu', root))
root.geometry(str(conf['root']['window']['geometry']['width']) + 'x' + str(conf['root']['window']['geometry']['height']))
root.resizable(0,0) if not conf['root']['window']['geometry']['resizable'] else root.resizable(conf['root']['window']['geometry']['resizable']['width'], conf['root']['window']['geometry']['resizable']['height'])

# Pack Built GUI Frames Into 'root' Window
Intro(root).pack()
Path(root).pack()
License(root).pack()
Controls(root).pack()

# Initiate Event Loop
root.mainloop()
