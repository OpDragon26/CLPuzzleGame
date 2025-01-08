import clgame
import timer
import levels
from pynput.keyboard import *

level = 0

levels.level1.update()

playerPos = [0,20]

timer = timer.Timer()
timer.startTimer()

class v1:
    doors = True
    spacePressed = 0

def on_press(key):
    global v1, timer, level
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

    elif key == Key.space:
        if timer.getTimer() - 1 > v1.spacePressed:
            v1.spacePressed = timer.getTimer()
            if level == 0:
                for hitbox in levels.levels[level].collideHitboxes(playerPos):
                    if "lever" in hitbox.tags:
                        v1.doors = not v1.doors

    elif key == Key.esc: return False

    if levels.levels[level].hitboxes["finish"].collidePoint(playerPos):
        level = 1
        plyerPos = [0,20]

    if level == 0:
        levels.levels[level].textures["door1"].shown = v1.doors
        levels.levels[level].textures["door2"].shown = not v1.doors

        levels.levels[level].textures["door1_open"].shown = not v1.doors
        levels.levels[level].textures["door2_open"].shown = v1.doors

        levels.levels[level].textures["lever1"].shown = not v1.doors
        levels.levels[level].textures["lever1_on"].shown = v1.doors

        levels.levels[level].textures["lever2"].shown = not v1.doors
        levels.levels[level].textures["lever2_on"].shown = v1.doors

        levels.levels[level].hitboxes["door1"].active = not v1.doors
        levels.levels[level].hitboxes["door2"].active = v1.doors

    levels.levels[level].moveText("player",(playerPos[0] * 2 + 1, playerPos[1]))
    levels.levels[level].update()

with Listener(on_press = on_press) as listener:
    listener.join()
