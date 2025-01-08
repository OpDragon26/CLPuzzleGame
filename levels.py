import clgame

wall = clgame.Texture("textures/wall.txt") # Hitbox height: 
lever = clgame.Texture("textures/lever.txt")
leverOn = clgame.Texture("textures/lever_on.txt")
player =  clgame.Text("P",(0,20))


level1 = clgame.Scene(texture=clgame.Texture("level_empty.txt"))

level1.addTexture(wall,"wall1",(20,0))
level1.addTexture(wall,"wall2",(35,0))
level1.addText(player,"player")
level1.addHitbox(clgame.Hitbox((20,0),(2,39),["wall"]),"wall1")

levels = [level1]