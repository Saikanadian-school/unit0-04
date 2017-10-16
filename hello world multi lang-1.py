#coding: utf-8

# Created by: Anthony Freeman
# Created on: September 2017
# Created for: ICS3U

import ui

def english_button(sender):
    view['hello_world_label'].text = ('Hello, World!')
    
def french_button(sender):
    view['hello_world_label'].text = ('Bonjour le monde!')
    
def spanish_button(sender):
    view['hello_world_label'].text = ('Hola Mundo!')

view = ui.load_view()
view.present('full_screen')
