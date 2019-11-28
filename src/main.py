from tkinter import *
from lib.load import load
from lib.pack import pack

conf = load('yaml')

root = Tk()
root.title(conf['root']['window']['title'])
root.config(menu=load('menu', root))
root.geometry(str(conf['root']['window']['geometry']['width']) + 'x' + str(conf['root']['window']['geometry']['height']))
root.resizable(0,0) if not conf['root']['window']['geometry']['resizable'] else root.resizable(conf['root']['window']['geometry']['resizable']['width'], conf['root']['window']['geometry']['resizable']['height'])

##### pack frames here #####
# first: import actual frames
# then: pass it to the function
pack('header', root)
pack('head', root)
pack('body', root)
pack('footer', root)

root.mainloop()
