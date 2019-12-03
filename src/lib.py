from tkinter import *
import webbrowser
import yaml
import sys

TkMenu = Menu


def config():
    with open('config.yml') as file:
        data = yaml.load(file, Loader=yaml.FullLoader)
        return data


def platform():
    if sys.platform.startswith('linux'):
        return 'linux'
    elif sys.platform.startswith('win32') or sys.platform.startswith('cygwin'):
        return 'windows'
    elif sys.platform.startswith('darwin'):
        return 'darwin'
    else:
        return 'Undetected operating system type.'


conf = config()


def Title(target):
    return target.title(conf['root']['title'])


def Menu(target):
    if conf['root']['menu']:
        menu = TkMenu(target)
        # build menu using data from Config()
        return target.config(menu=menu)
    else:
        menu = TkMenu(target)
        return target.config(menu=menu)


def Geometry(target):
    geostr = str(conf['root']['geometry']['width'])+'x'+str(conf['root']['geometry']['height'])
    return target.geometry(geostr)


def Font(obj):
    font = obj['family']+' '+str(obj['size'])+' '+obj['style']
    return font


def Resize(target):
    if conf['root']['geometry']['resizable']:
        return target.resizable(0,0)
    else:
        return target.resizable(0,0)


def OpenLink():
    webbrowser.open_new_tab(conf['root']['content']['intro']['description']['link'])


def SetPath():
    print('setting path ...')
    return 'asdsdsds'


def ChangePath(args):
    print('changing path ...')


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

def Quit(args):
    sys.exit()

def Install(args):
    print('installing binaries...')
