from tkinter import *
import webbrowser
import yaml

# Alias the namespace of tkinter's Menu method
TkMenu = Menu

# Config Function
# returns python dictionary
# containing data from config.yml
def Config():
    with open('config.yml') as file:
        data = yaml.load(file, Loader=yaml.FullLoader)
        return data

# Call Config() to set conf as the data object
# which is used in the other functions as well.
conf = Config()

# Title Function
# returns window title
def Title(target):
    return target.title(conf['root']['title'])

# Menu Function
# returns window menu
def Menu(target):
    if conf['root']['menu']:
        menu = TkMenu(target)
        # build menu using data from Config()
        return target.config(menu=menu)
    else:
        menu = TkMenu(target)
        return target.config(menu=menu)

# Geometry Function
# returns window geometry
def Geometry(target):
    geostr = str(conf['root']['geometry']['width']) + 'x' + str(conf['root']['geometry']['height'])
    return target.geometry(geostr)

def Font(obj):
    font = obj['family'] + ' ' + str(obj['size']) + ' ' + obj['style']
    return font

# Resize Function
# returns window resize configuration
def Resize(target):
    if conf['root']['geometry']['resizable']:
        return target.resizable(0,0)
    else:
        return target.resizable(0,0)

if conf['root']['content']['intro']['description']['link']:
    def Openlink0():
        webbrowser.open_new_tab(conf['root']['content']['intro']['description']['link'])

def Openlink1(args):
    print('asd')

# Text Linker
# make certain tkinter Text characters
# clickable with correspanding functions
class Link:
    def __init__(self, text):
        self.text = text
        self.text.tag_config('hyper', foreground='blue')
        self.text.tag_bind('hyper', '<Enter>', self._enter)
        self.text.tag_bind('hyper', '<Leave>', self._leave)
        self.text.tag_bind('hyper', '<Button-1>', self._click)
        self.reset()
    def reset(self):
        self.links = {}
    def add(self, action):
        tag = 'hyper-%d' % len(self.links)
        self.links[tag] = action
        return 'hyper', tag
    def _enter(self, event):
        self.text.config(cursor='')
    def _leave(self, event):
        self.text.config(cursor='')
    def _click(self, event):
        for tag in self.text.tag_names(CURRENT):
            if tag[:6] == 'hyper-':
                self.links[tag]()
                return
