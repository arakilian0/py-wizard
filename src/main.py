from tkinter import Tk
from lib import Title, Menu, Geometry, Resize
from frame import Intro, Path

root = Tk()

Title(root)
Menu(root)
Geometry(root)
Resize(root)

Intro(root).pack()
Path(root).pack()
# License(root).pack()
# Control(root).pack()

root.mainloop()
