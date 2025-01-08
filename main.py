import clgame
import levels
from pynput.keyboard import *

level = 0

levels.level1.update()

playerPos = [0,20]

def on_press(key):
    if key == Key.right:
        playerPos[0] += 1

        collide = False
        for hitbox in levels.levels[level].collideHitboxes(playerPos):
            if "wall" in hitbox.tags:
                collide = True
            elif "door" in hitbox.tags:
                collide = False
                break
        if collide:
            playerPos[0] -= 1

    elif key == Key.left:
        playerPos[0] -= 1

        collide = False
        for hitbox in levels.levels[level].collideHitboxes(playerPos):
            if "wall" in hitbox.tags:
                collide = True
            elif "door" in hitbox.tags:
                collide = False
                break
        if collide:
            playerPos[0] += 1
    elif key == Key.down:
        playerPos[1] += 1

        collide = False
        for hitbox in levels.levels[level].collideHitboxes(playerPos):
            if "wall" in hitbox.tags:
                collide = True
            elif "door" in hitbox.tags:
                collide = False
                break
        if collide:
            playerPos[1] -= 1

    elif key == Key.up:
        playerPos[1] -= 1

        collide = False
        for hitbox in levels.levels[level].collideHitboxes(playerPos):
            if "wall" in hitbox.tags:
                collide = True
            elif "door" in hitbox.tags:
                collide = False
                break
        if collide:
            playerPos[1] += 1
        

    elif key == Key.esc: return False
    levels.levels[level].moveText("player",(playerPos[0] * 2 + 1, playerPos[1]))
    levels.levels[level].update()

with Listener(on_press = on_press) as listener:
    listener.join()
