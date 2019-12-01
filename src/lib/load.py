from tkinter import *
import yaml

def Load(type, target='config.yml'):

    # yaml file loader
    if type == 'yaml':
        with open(target) as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            return data

    # tkinter menu loader
    if type == 'menu' and target:
        with open('config.yml') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            if not data['root']['window']['menu']:
                return Menu(target)
            # else:
            #     menu = Menu(target)
            #     create custom menu items here
            #     return menu
