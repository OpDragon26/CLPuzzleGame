import clgame

wall = clgame.Texture("textures/wall.txt")
door = clgame.Texture("textures/door.txt")
door_open = clgame.Texture("textures/door_open.txt")
lever = clgame.Texture("textures/lever.txt")
lever_on = clgame.Texture("textures/lever_on.txt")
player =  clgame.Text("P",(0,20))


level1 = clgame.Scene(texture=clgame.Texture("level_empty.txt"))

level1.addTexture(wall,"wall1",(20,0))
level1.addTexture(wall,"wall2",(35,0))

level1.addTexture(door, "door1",(20,27))
level1.addTexture(door, "door2",(35,10))

level1.addTexture(door_open, "door1_open",(20,27))
level1.addTexture(door_open, "door2_open",(35,10))
level1.hideTexture("door1_open")

level1.addTexture(lever,"lever1",(10,32))
level1.addTexture(lever_on,"lever1_on",(10,32))

level1.addTexture(lever,"lever2",(27,32))
level1.addTexture(lever_on,"lever2_on",(27,32))

level1.addText(player,"player")

level1.addHitbox(clgame.Hitbox((20,0),(2,39),["wall"]),"wall1")
level1.addHitbox(clgame.Hitbox((35,0),(2,39),["wall"]),"wall2")

level1.addHitbox(clgame.Hitbox((20,27),(2,2),["door"]),"door1")
level1.addHitbox(clgame.Hitbox((35,10),(2,2),["door"]),"door2")

level1.addHitbox(clgame.Hitbox((9,31),(3,3),["lever"]),"lever1")
level1.addHitbox(clgame.Hitbox((26,31),(3,3),["lever"]),"lever2")

level1.addHitbox(clgame.Hitbox((60,0),(2,39)),"finish")

levels = [level1] 