import clgame
from pynput.keyboard import *

levels = [
    clgame.Scene(fileImport=clgame.Texture("level_empty.txt"))
    ]
level = 0

def on_press(key):
    if key == Key.space:
        levels[level].update()
    elif key == Key.esc: return False
    
with Listener(on_press = on_press) as listener:
    listener.join()