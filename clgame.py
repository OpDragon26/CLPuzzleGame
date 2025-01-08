import os
from copy import deepcopy as copy

skipCharacter = "¤"

class Scene:
    def __init__(self, size=(0,0), backgroundCharacter="#", fileImport=None): # Either size or fileImport has to be given. size = (width, height)
        if fileImport == None:
            self.width = size[0]
            self.height = size[1]
            self.canvas = [[backgroundCharacter for i in range(self.width)] for i in range(self.height)]
        else:
            self.canvas = fileImport.texture
            self.height = len(self.canvas)
            self.width = len(self.canvas[0])
        
        self.baseCanvas = copy(self.canvas)

        self.hitboxes = {}
        self.textures = {}
        self.texts = {}
        self.textureOverlay = [[skipCharacter for i in range(self.width)] for i in range(self.height)]
        self.textOverlay = [[skipCharacter for i in range(self.width * 2 - 1)] for i in range(self.height * 2 - 1)]

    def replace(self, char, key):
        return key[char]

    def drawTextures(self):
        self.textureOverlay = [[skipCharacter for i in range(self.width)] for i in range(self.height)]

        for texture in self.textures.values():
            if texture.shown:
                for i in range(len(texture.texture.texture)):
                    for j in range(len(texture.texture.texture[0])):
                        self.textureOverlay[texture.pos[1] + i][texture.pos[0] + j] = texture.texture.texture[i][j]

    def drawTexts(self):
        self.textOverlay = [[skipCharacter for i in range(self.width * 2 - 1)] for i in range(self.height * 2 - 1)]

        for text in self.texts.values():
            if text.shown:
                match text.align:
                    case 0: startPosition = text.pos
                    case 1: startPosition = (text.pos[0] - int(len(text.text) / 2), text.pos[1])
                    case 2 : startPosition = (text.pos[0] - len(text.text) + 1, text.pos[1])
                for i in range(len(text.text)):
                    self.textOverlay[startPosition[1]][startPosition[0] + (i * (1 + text.spaced))] = text.text[i]


    def createPrint(self, replace={"":""}, skip=[]):

        for i in range(self.height):
            for j in range(self.width):
                if self.textureOverlay[i][j] == skipCharacter:
                    if self.canvas[i][j] in skip:
                        self.canvas[i][j] = " "
                    elif self.canvas[i][j] in replace.keys():
                        self.canvas[i][j] = self.replace(self.canvas[i][j], replace)
                else:
                    self.canvas[i][j] = self.textureOverlay[i][j]

        self.canvas = [[x for x in ' '.join(row)] for row in self.canvas]

        for i in range(self.height * 2 - 1):
            for j in range(self.width * 2 - 1):
                if self.textOverlay[i][j] != skipCharacter:
                    self.canvas[i][j] = self.textOverlay[i][j]


        return '\n'.join([''.join(row) for row in self.canvas])
    
    def update(self):
        self.drawTextures()
        self.drawTexts()
        printString = self.createPrint()
        os.system('cls' if os.name == 'nt' else 'clear')
        print(printString)
        self.canvas = copy(self.baseCanvas)

    def showTexture(self, texture):
        self.textures[texture].shown = True

    def hideTexture(self, texture):
        self.textures[texture].shown = False

    def moveTexture(self, texture, pos):
        self.textures[texture].pos = pos

    def activateHitbox(self, hitbox):
        self.hitboxes[hitbox].active = True

    def deactivateHitbox(self, hitbox):
        self.hitboxes[hitbox].active = False

    def moveHitbox(self, hitbox, pos):
        self.hitboxes[hitbox].pos = pos

    def hideText(self, text):
        self.texts[text].shown = False

    def showText(self, text):
        self.texts[text].shown = True

    def moveText(self, text, pos):
        self.texts[text].pos = pos


    def addHitbox(self, hitbox, name):
        self.hitboxes[name] = hitbox

    def addTexture(self, texture, name, pos):
        self.textures[name] = DrawnTexture(texture, pos)

    def addText(self, text, name):
        self.texts[name] = text
    
class Hitbox:
    def __init__(self, pos, size): # pos = (x, y), size = (width, height)
        self.pos = pos
        self.size = size
        self.active = True

    def collidePoint(self, point):
        return point[0] >= self.pos[0] and point[0] < self.pos[0] + self.size[0] and point[1] >= self.pos[1] and point[1] < self.pos[1] + self.size[1] and self.active
    
class Texture:
    def __init__(self, fileName):
        file = open(fileName)
        self.texture = [[j for j in row] for row in file.read().split("\n")]

class DrawnTexture:
    def __init__(self, texture, pos):
        self.texture = texture
        self.pos = pos
        self.shown = True

class Text:
    def __init__(self, text, pos, align=0, spaced=False): 
        self.text = text
        self.pos = pos
        self.align = align # 0 - left, 1 - center, 2 - right
        self.spaced = spaced # Whether the're should be a space between the letters, like any other characters
        self.shown = True