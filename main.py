import pygame, os, math, numpy as np, random
from pygame.locals import *
pygame.init()

black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 128, 0)
brown = (139,69,19)
red = (255, 0, 0)
grey = (128,128,128)

lightGrey = (211,211,211)

clock = pygame.time.Clock()
vec = pygame.math.Vector2


FlexyPath = os.path.dirname(os.path.abspath(__file__))
screenSize = (1620 , 1000)

NWQuadrant = [[657, 2428, 338, 254], [1126, 2372, 345, 310], [230, 1637, 37, 100], [314, 1441, 51, 9], [1077, 2281, 30, 9], [601, 2855, 114, 93], [1245, 3205, 72, 37], [2372, 3023, 44, 23], [2449, 2449, 58, 44], [2918, 2631, 72, 65], [2932, 1791, 51, 37], [2820, 594, 65, 44], [321, 3394, 51, 23],[3282, 888, 163, 100]]
NEQuadrant = [[3310, 895, 128, 93], [3667, 27, 16, 982], [3667, 1434, 16, 590], [3716, 2001, 3257, 23], [6992, 41, -19, 1990], [3681, 34, 3257, 44], [4136, 132, 527, 786], [4787, 314, 793, 527], [5270, 825, 317, 261], [5711, 265, 1087, 590], [3807, 1357, 576, 380], [4563, 1357, 562, 380], [5487, 1350, 576, 387], [6243, 1357, 555, 387], [3968, 1231, 331, 51], [4668, 1231, 408, 51], [5732, 1224, 142, 37], [6327, 1238, 394, 44], [4500, 2183, 72, 37], [4591, 2449, 72, 44], [3492, 2393, 142, 100], [3996, 2407, 282, 450], [4185, 2295, 261, 219], [4745, 2085, 653, 394], [5606, 2085, 289, 359], [4773, 2099, 2186, 2130], [4129, 3450, 282, 436], [4430, 3632, 233, 436]]
SWQuadrant = [[293, 4927, 814, 359], [419, 4773, 310, 51], [1672, 4899, 555, 380], [2400, 4815, 457, 464], [3016, 4829, 527, 443], [1791, 4766, 338, 37], [3100, 4689, 380, 72], [3569, 5263, 156, 128], [3870, 5536, 58, 51], [3779, 5844, 121, 86], [3394, 5753, 296, 170], [3219, 6180, 492, 597], [2750, 6719, 345, 226], [1784, 5963, 1087, 408], [2190, 5795, 324, 79], [314, 5823, 534, 779], [41, 4584, 1157, 58], [1231, 4423, 65, 205], [1686, 4423, 100, 198], [1826, 4570, 2228, 79],[307, 4227, 65, 37], [3303, 4500, 65, 44], [3478, 4164, 142, 65], [3779, 4045, 37, 16], [3121, 3590, 58, 23]]
SEQuadrant = [[4101, 3506, 2851, 464], [4458, 3891, 2494, 289], [4752, 4101, 2214, 86], [4892, 4220, 2074, 317], [5214, 4479, 1745, 149], [5508, 4633, 520, 149], [6481, 4689, 205, 205], [5053, 4983, 156, 107], [4976, 4521, 65, 30], [5795, 5165, 79, 30], [4787, 6278, 156, 114], [4689, 6677, 142, 135], [4878, 6544, 604, 44], [5046, 6726, 163, 142], [5095, 6341, 100, 65], [5361, 5998, 401, 37], [5998, 5557, 142, 93], [5466, 5893, 359, 30], [6005, 5564, 926, 1332], [5543, 6089, 779, 856], [5060, 6306, 877, 646], [4017, 4577, 51, 2291], [3401, 5746, 289, 184], [3772, 5837, 114, 86], [3856, 5550, 65, 23], [3590, 5277, 142, 114], [3226, 6180, 485, 590],[3107, 4591, 961, 51], [3471, 4150, 135, 93], [3779, 4059, 44, 9]]

window = pygame.display.set_mode(screenSize)
# enemySpriteNsc = [pygame.image.load(FlexyPath + "/Sprites/Mobs/Cactus/FrontW/tile011.png"), pygame.image.load(FlexyPath + "/Sprites/Mobs/Cactus/tile012.png"), pygame.image.load(FlexyPath + "/Sprites/Mobs/Cactus/tile013.png"), pygame.image.load(FlexyPath + "/Sprites/Mobs/Cactus/tile014.png"), pygame.image.load(FlexyPath + "/Sprites/Mobs/Cactus/tile015.png"), pygame.image.load(FlexyPath + "/Sprites/Mobs/Cactus/tile016.png"), pygame.image.load(FlexyPath + "/Sprites/Mobs/Cactus/tile017.png"), pygame.image.load(FlexyPath + "/Sprites/Mobs/Cactus/tile018.png"), pygame.image.load(FlexyPath + "/Sprites/Mobs/Cactus/tile019.png"), pygame.image.load(FlexyPath + "/Sprites/Mobs/Cactus/tile020.png")]
playerSpriteNscF = [pygame.image.load(FlexyPath + "/Sprites/Player/FrontW/tile014.png"), pygame.image.load(FlexyPath + "/Sprites/Player/FrontW/tile015.png"), pygame.image.load(FlexyPath + "/Sprites/Player/FrontW/tile016.png"), pygame.image.load(FlexyPath + "/Sprites/Player/FrontW/tile017.png"), pygame.image.load(FlexyPath + "/Sprites/Player/FrontW/tile018.png"), pygame.image.load(FlexyPath + "/Sprites/Player/FrontW/tile019.png"), pygame.image.load(FlexyPath + "/Sprites/Player/FrontW/tile020.png"), pygame.image.load(FlexyPath + "/Sprites/Player/FrontW/tile021.png")]
playerSpriteNscR = [pygame.image.load(FlexyPath + "/Sprites/Player/SideW/tile014.png"), pygame.image.load(FlexyPath + "/Sprites/Player/SideW/tile015.png"), pygame.image.load(FlexyPath + "/Sprites/Player/SideW/tile016.png"), pygame.image.load(FlexyPath + "/Sprites/Player/SideW/tile017.png"), pygame.image.load(FlexyPath + "/Sprites/Player/SideW/tile018.png"), pygame.image.load(FlexyPath + "/Sprites/Player/SideW/tile019.png"), pygame.image.load(FlexyPath + "/Sprites/Player/SideW/tile020.png"), pygame.image.load(FlexyPath + "/Sprites/Player/SideW/tile021.png")]
playerSpriteNscL = [pygame.transform.flip(pygame.image.load(FlexyPath + "/Sprites/Player/SideW/tile014.png"), True, False), pygame.transform.flip(pygame.image.load(FlexyPath + "/Sprites/Player/SideW/tile015.png"), True, False), pygame.transform.flip(pygame.image.load(FlexyPath + "/Sprites/Player/SideW/tile016.png"), True, False), pygame.transform.flip(pygame.image.load(FlexyPath + "/Sprites/Player/SideW/tile017.png"), True, False), pygame.transform.flip(pygame.image.load(FlexyPath + "/Sprites/Player/SideW/tile018.png"), True, False), pygame.transform.flip(pygame.image.load(FlexyPath + "/Sprites/Player/SideW/tile019.png"), True, False), pygame.transform.flip(pygame.image.load(FlexyPath + "/Sprites/Player/SideW/tile020.png"), True, False), pygame.transform.flip(pygame.image.load(FlexyPath + "/Sprites/Player/SideW/tile021.png"), True, False)]
playerSpriteNscB = [pygame.image.load(FlexyPath + "/Sprites/Player/BackW/tile014.png"), pygame.image.load(FlexyPath + "/Sprites/Player/BackW/tile015.png"), pygame.image.load(FlexyPath + "/Sprites/Player/BackW/tile016.png"), pygame.image.load(FlexyPath + "/Sprites/Player/BackW/tile017.png"), pygame.image.load(FlexyPath + "/Sprites/Player/BackW/tile018.png"), pygame.image.load(FlexyPath + "/Sprites/Player/BackW/tile019.png"), pygame.image.load(FlexyPath + "/Sprites/Player/BackW/tile020.png"), pygame.image.load(FlexyPath + "/Sprites/Player/BackW/tile021.png")]


enemySpriteNscF = [pygame.image.load(FlexyPath + "/Sprites/Mobs/Cactus/FrontW/tile014.png"), pygame.image.load(FlexyPath + "/Sprites/Mobs/Cactus/FrontW/tile015.png"), pygame.image.load(FlexyPath + "/Sprites/Mobs/Cactus/FrontW/tile016.png"), pygame.image.load(FlexyPath + "/Sprites/Mobs/Cactus/FrontW/tile017.png"), pygame.image.load(FlexyPath + "/Sprites/Mobs/Cactus/FrontW/tile018.png"), pygame.image.load(FlexyPath + "/Sprites/Mobs/Cactus/FrontW/tile019.png"), pygame.image.load(FlexyPath + "/Sprites/Mobs/Cactus/FrontW/tile020.png")]
enemySpriteNscR = [pygame.image.load(FlexyPath + "/Sprites/Mobs/Cactus/SideW//tile014.png"), pygame.image.load(FlexyPath + "/Sprites/Mobs/Cactus/SideW//tile015.png"), pygame.image.load(FlexyPath + "/Sprites/Mobs/Cactus/SideW//tile016.png"), pygame.image.load(FlexyPath + "/Sprites/Mobs/Cactus/SideW//tile017.png"), pygame.image.load(FlexyPath + "/Sprites/Mobs/Cactus/SideW//tile018.png"), pygame.image.load(FlexyPath + "/Sprites/Mobs/Cactus/SideW//tile019.png"), pygame.image.load(FlexyPath + "/Sprites/Mobs/Cactus/SideW//tile020.png")]
enemySpriteNscL = [pygame.transform.flip(pygame.image.load(FlexyPath + "/Sprites/Mobs/Cactus/SideW//tile014.png"), True, False), pygame.transform.flip(pygame.image.load(FlexyPath + "/Sprites/Mobs/Cactus/SideW//tile015.png"), True, False), pygame.transform.flip(pygame.image.load(FlexyPath + "/Sprites/Mobs/Cactus/SideW//tile016.png"), True, False), pygame.transform.flip(pygame.image.load(FlexyPath + "/Sprites/Mobs/Cactus/SideW//tile017.png"), True, False), pygame.transform.flip(pygame.image.load(FlexyPath + "/Sprites/Mobs/Cactus/SideW//tile018.png"), True, False), pygame.transform.flip(pygame.image.load(FlexyPath + "/Sprites/Mobs/Cactus/SideW//tile019.png"), True, False), pygame.transform.flip(pygame.image.load(FlexyPath + "/Sprites/Mobs/Cactus/SideW//tile020.png"), True, False)]
enemySpriteNscB = [pygame.image.load(FlexyPath + "/Sprites/Mobs/Cactus/BackW/tile014.png"), pygame.image.load(FlexyPath + "/Sprites/Mobs/Cactus/BackW/tile015.png"), pygame.image.load(FlexyPath + "/Sprites/Mobs/Cactus/BackW/tile016.png"), pygame.image.load(FlexyPath + "/Sprites/Mobs/Cactus/BackW/tile017.png"), pygame.image.load(FlexyPath + "/Sprites/Mobs/Cactus/BackW/tile018.png"), pygame.image.load(FlexyPath + "/Sprites/Mobs/Cactus/BackW//tile019.png"), pygame.image.load(FlexyPath + "/Sprites/Mobs/Cactus/BackW/tile020.png")]

gun = [pygame.transform.flip(pygame.image.load(FlexyPath + "/Sprites/Gun/0.png"), True, False), pygame.transform.flip(pygame.image.load(FlexyPath + "/Sprites/Gun/1.png"), True, False), pygame.transform.flip(pygame.image.load(FlexyPath + "/Sprites/Gun/2.png"), True, False), pygame.transform.flip(pygame.image.load(FlexyPath + "/Sprites/Gun/3.png"), True, False), pygame.transform.flip(pygame.image.load(FlexyPath + "/Sprites/Gun/4.png"), True, False), pygame.transform.flip(pygame.image.load(FlexyPath + "/Sprites/Gun/5.png"), True, False), pygame.transform.flip(pygame.image.load(FlexyPath + "/Sprites/Gun/6.png"), True, False), pygame.transform.flip(pygame.image.load(FlexyPath + "/Sprites/Gun/7.png"), True, False), pygame.transform.flip(pygame.image.load(FlexyPath + "/Sprites/Gun/8.png"), True, False), pygame.transform.flip(pygame.image.load(FlexyPath + "/Sprites/Gun/9.png"), True, False)]

healthHeart = pygame.image.load(FlexyPath + "/Sprites/Misc/heart.png")
healthHeart = pygame.transform.scale(healthHeart, (50, 50)) 

coin = pygame.image.load(FlexyPath + "/Sprites/Misc/coin.png")
coin = pygame.transform.scale(coin, (50, 50)) 

font = pygame.font.Font('freesansbold.ttf', 26)


enemySprite = []
enemySpriteF = []
enemySpriteR = []
enemySpriteL = []
enemySpriteB = []

playerSpriteF = []
playerSpriteR = []
playerSpriteL = []
playerSpriteB = []

rectMapNW = []
rectMapNE = []
rectMapSW = []
rectMapSW = []



bullets = []
enemies = []





for i in enemySpriteNscF:
    i = pygame.transform.scale(i, (100, 100))
    i.convert()
    enemySpriteF.append(i)

for i in enemySpriteNscR:
    i = pygame.transform.scale(i, (100, 100))
    i.convert()
    enemySpriteR.append(i)

for i in enemySpriteNscL:
    i = pygame.transform.scale(i, (100, 100))
    i.convert()
    enemySpriteL.append(i)
    
for i in enemySpriteNscB:
    i = pygame.transform.scale(i, (100, 100))
    i.convert()
    enemySpriteB.append(i)


for i in playerSpriteNscF:
    i = pygame.transform.scale(i, (100, 100))
    i.convert()
    playerSpriteF.append(i)

for i in playerSpriteNscR:
    i = pygame.transform.scale(i, (100, 100))
    i.convert()
    playerSpriteR.append(i)

for i in playerSpriteNscL:
    i = pygame.transform.scale(i, (100, 100))
    i.convert()
    playerSpriteL.append(i)
    
for i in playerSpriteNscB:
    i = pygame.transform.scale(i, (100, 100))
    i.convert()
    playerSpriteB.append(i)



bg = pygame.image.load(FlexyPath + "/map.png").convert()
minimap = pygame.image.load(FlexyPath + "/miniMap.png").convert()

class player(object):
    def __init__(self, x, y, width, height):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.speed = 10
        self.health = 100
        self.bulletDamage = 20
        self.rot = 0
        self.changeSprite = 0
        self.shoot = False
        self.money = 0
        self.rect = pygame.Rect(self.x, self.y, 100, 100)

    def draw(self, window, playerSpriteR):
        for i in enemies:
            if self.rect.colliderect(i.rect) == 1:
                self.health -= 0.10
            
            
        self.pos = vec(self.x, self.y)
        if self.changeSprite > 38:
            self.changeSprite = -1
        self.changeSprite += 1
        window.blit(playerSpriteR[self.changeSprite//5], (self.x, self.y))


class shooting(object):
    def __init__(self, playerx, playery, mouse):

        self.camx = background.x
        self.camy = background.y
        self.playerx = playerx
        self.playery = playery
        self.x = playerx + 50
        self.y = playery + 50
        self.Playerpos = vec(playerx + 50, playery + 50)
        self.rot = (vec(mouse) - self.Playerpos).angle_to(vec(1, 0)) + 90

        
        if self.rot < 0:
            self.rot += 360


        self.shoot = True
        bullets.append(self)
    def draw(self, window):
        self.collideT = False
        self.rect = pygame.Rect(self.x, self.y, 10, 10)
        self.x = self.x + (15*math.sin(math.radians(self.rot)))
        self.y = self.y + (15*math.cos(math.radians(self.rot)))
        if self.camx != background.x:
            self.x += (self.camx - background.x)
            self.camx = background.x
        if self.camy != background.y:
            self.y += (self.camy - background.y)
            self.camy = background.y
        if self.x < 0 or self.x > screenSize[0] or self.y < 0 or self.y > screenSize[1]:
            bullets.remove(self)
            self.collideT = True
        
        if self.collideT == False:
            for i in enemies:
                if self.rect.colliderect(i.rect) == 1:
                    bullets.remove(self)
                    self.collideT = True
                    if i.health - mainPlayer.bulletDamage > 0:
                        i.health -= mainPlayer.bulletDamage
                    else:
                        enemies.remove(i)
                        mainPlayer.money += 10
                    break

        
        if self.collideT == False:
            if checkCollision(self.x, self.y, True) == False:
                bullets.remove(self)

        pygame.draw.circle(window, black, (self.x,self.y), 10)

class walls(object):
    def __init__(self):
        self.rectMapNW = []
        self.rectMapNE = []
        self.rectMapSW = []
        self.rectMapSW = []
    def draw(self):
        for i in NWQuadrant:
            self.rectMapNW.append(pygame.Rect(i[0] - background.x, i[1] - background.y, i[2], i[3]))
        for i in NEQuadrant:
            self.rectMapNE.append(pygame.Rect(i[0] - background.x, i[1] - background.y, i[2], i[3]))
        for i in SWQuadrant:
            self.rectMapSW.append(pygame.Rect(i[0] - background.x, i[1] - background.y, i[2], i[3]))
        for i in SWQuadrant:
            self.rectMapSW.append(pygame.Rect(i[0] - background.x, i[1] - background.y, i[2], i[3]))
        
class enemy(object):
    def __init__(self, x, y, width, height, speed):
        self.width = width
        self.height = height
        self.speed = speed
        self.x = x
        self.y = y
        self.health = 50
        self.changeSprite = 0
        self.rot = 0
        self.searchArea = 2000
        self.rect = pygame.Rect(self.x, self.y, 100, 100)
        enemies.append(self)
    def draw(self, window):
        self.rect = pygame.Rect(self.x, self.y, 100, 100)
        self.pos = vec(self.x, self.y)
        self.rot = (mainPlayer.pos - self.pos).angle_to(vec(1, 0))
        if self.rot < 0:
            self.rot += 360
        enemySprite = enemySpriteF

        if self.rot >= 225 and self.rot <= 315:
            enemySprite = enemySpriteF
        if self.rot >= 45 and self.rot <= 135:
            enemySprite = enemySpriteB
        if self.rot > 135 and self.rot < 225:
            enemySprite = enemySpriteL
        if self.rot < 45 or self.rot > 315:
            enemySprite = enemySpriteR

        if abs(self.y - mainPlayer.y) < self.searchArea and abs(self.x - mainPlayer.y) < self.searchArea:
            
            if self.y < mainPlayer.y:
                if checkCollision(self.x + 50, self.y + 65.5 + self.speed, False) == True:
                    self.y += self.speed
            
            if self.y > mainPlayer.y:
                if checkCollision(self.x + 50, self.y + 65.5 - self.speed, False) == True:
                    self.y -= self.speed
        
            if self.x > mainPlayer.x:
                if checkCollision(self.x + 50 - self.speed, self.y + 65.5, False) == True:
                    self.x -= self.speed
        
            if self.x < mainPlayer.x:
                if checkCollision(self.x + 50 + self.speed, self.y + 65.5, False) == True:
                    self.x += self.speed


        if self.changeSprite > 33:
            self.changeSprite = -1
        self.changeSprite += 1
        playerSprite = playerSpriteB
        window.blit(enemySprite[self.changeSprite//5], (self.x, self.y))

        
class miniMap(object):
    def __init__(self):
        self.x = 1300
        self.y = 50
    def draw(self, window):
        if mainPlayer.x > 1300 and mainPlayer.y < 210+50:
            self.x = 50
        else:
            self.x = 1300 + 100

        window.blit(minimap, (self.x, self.y))
        pygame.draw.rect(window, red, pygame.Rect((mainPlayer.x + background.x)/35 + self.x, (mainPlayer.y + background.y)/35 + self.y, 3, 3))


class background(object):
    def __init__(self, x, y, width, height):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
    def draw(self, window):
        window.blit(bg, (0 - self.x, 0 - self.y))



def textRender(text, font , colour):
    textSurface = font.render(text, True, colour)
    return textSurface, textSurface.get_rect()

def showText(text, fontSize, textloc, colour):
    Font = pygame.font.Font(FlexyPath + '/Font.ttf', fontSize)
    finalText, textLoc = textRender(text, Font , colour)
    window.blit(finalText, textloc)
    
def ammo():
    global changeSpritez
    global Reload
    global shots
    if Reload == True:
        if changeSpritez > 64:
            Reload = False
            shots = 6
            changeSpritez = -1
        changeSpritez += 1
        window.blit(gun[changeSpritez//8], (1200, 500))

def enemyHealthBar(i):
    if i.health != 50:
            pygame.draw.rect(window, "red", pygame.Rect(i.x+24, i.y+105, 50, 5))
            pygame.draw.rect(window, "green", pygame.Rect(i.x+24, i.y+105, i.health, 5))

def playerHealthBar():
    pygame.draw.rect(window, "black", pygame.Rect(67, 867, 186, 36))
    pygame.draw.rect(window, "white", pygame.Rect(70, 870, 180, 30))
    if mainPlayer.health > 75:
        pygame.draw.rect(window, "green", pygame.Rect(70, 870, round(mainPlayer.health*(180/100)), 30))
    elif mainPlayer.health > 25:
        pygame.draw.rect(window, (255, 185, 0), pygame.Rect(70, 870, round(mainPlayer.health*(180/100)), 30))
    else:
        pygame.draw.rect(window, "red", pygame.Rect(70, 870, round(mainPlayer.health*(180/100)), 30))
    # heart (x,y)= (barX - 34, barY - 12)
    window.blit(healthHeart, (36, 858))

def checkCollision(xPos, yPos, shoot):

    yPos += background.y
    xPos += background.x

    if xPos > 3500:
        if yPos > 3500:
            objectList = SEQuadrant
        else:
            objectList = NEQuadrant
    else:
        if yPos < 3500:
            objectList = NWQuadrant
        else:
            objectList = SWQuadrant
    for i in range(0, len(objectList)):
    
        if shoot == False:
            if xPos > objectList[i][0] and xPos < objectList[i][0] + objectList[i][2] or xPos + mainPlayer.width/2 > objectList[i][0] and xPos + mainPlayer.width/2 < objectList[i][0] + objectList[i][2] or xPos - mainPlayer.width/2 > objectList[i][0] and xPos - mainPlayer.width/2 < objectList[i][0] + objectList[i][2]:
                if yPos > objectList[i][1] and yPos < objectList[i][1] + objectList[i][3] or yPos +  mainPlayer.height/2 > objectList[i][1] and yPos + mainPlayer.height/2 < objectList[i][1] + objectList[i][3] or yPos - mainPlayer.height/2 > objectList[i][1] and yPos - mainPlayer.height/2 < objectList[i][1] + objectList[i][3]:
                    return False
        else:
            if xPos > objectList[i][0] and xPos < objectList[i][0] + objectList[i][2] or xPos + 10/2 > objectList[i][0] and xPos + 10/2 < objectList[i][0] + objectList[i][2] or xPos - 10/2 > objectList[i][0] and xPos - 10/2 < objectList[i][0] + objectList[i][2]:
                if yPos > objectList[i][1] and yPos < objectList[i][1] + objectList[i][3] or yPos +  10/2 > objectList[i][1] and yPos + 10/2 < objectList[i][1] + objectList[i][3] or yPos - 10/2 > objectList[i][1] and yPos - 10/2 < objectList[i][1] + objectList[i][3]:
                    return False
    return True
Pause = False

def reDraw(playerS):
    global Pause
    global shots
    background.draw(window)
    mainPlayer.draw(window, playerS)
    for i in enemies:
        i.draw(window)
        enemyHealthBar(i)
    for i in bullets:
        i.draw(window)
    miniMap.draw(window)
    if Reload == True:
        ammo()
        
    else:
        window.blit(gun[0], (1200, 500))
    
    playerHealthBar()

    pygame.draw.rect(window, "black", pygame.Rect(57, 927, 136, 36))
    pygame.draw.rect(window, "white", pygame.Rect(60, 930, 130, 30))
    textsurface = font.render(str(mainPlayer.money), False, (0, 0, 0))
    showText(str(shots)+"/6", 60, (1400,900), black)
    showText("Enemies Remaining: " + str(len(enemies)), 40, (550,50), black)
    pause.draw()
    if pause.draw() == "pause":
        Pause = True

    if Pause == True:
        resume.draw()
        sound.draw()
        quit.draw()

    window.blit(textsurface, (95,932))
    window.blit(coin, (38, 920))

    walls.draw()
    for i in NEQuadrant:
        pygame.draw.rect(window, red, pygame.Rect(i[0] - background.x, i[1] - background.y, i[2], i[3]))
    for i in NWQuadrant:
        pygame.draw.rect(window, red, pygame.Rect(i[0] - background.x, i[1] - background.y, i[2], i[3]))
    for i in SEQuadrant:
        pygame.draw.rect(window, red, pygame.Rect(i[0] - background.x, i[1] - background.y, i[2], i[3]))
    for i in SWQuadrant:
        pygame.draw.rect(window, red, pygame.Rect(i[0] - background.x, i[1] - background.y, i[2], i[3]))

    pygame.display.flip()
    

class button(object):
    def __init__(self, x, y, text):
        self.x = x
        self.y = y
        self.text = text
        self.rectangle = pygame.Rect(self.x,self.y,240,50)
        self.msel = "Shares"
    def draw(self):
        # global marketSelected
        # global Found
        self.colour = lightGrey

        self.font = pygame.font.Font(FlexyPath + '/Font.ttf', 40)
        if self.rectangle.collidepoint(pygame.mouse.get_pos()):
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.msel = ""
                self.colour = black
                pygame.draw.rect(window, self.colour, self.rectangle)
                showText(self.text, 40, (self.x + 35, self.y + 5), black)
                return self.text

            else:
                self.colour = grey



        pygame.draw.rect(window, self.colour, self.rectangle)
        showText(self.text, 40, (self.x + (120 - self.font.size(self.text)[0]/2), self.y + 5), black)    


# def shop():
#     pause = button(600,400, "pause")

Reload = False
running = True
walls = walls()
background = background(0, 0, 7000, 7000)
enemyCount = 1
changeSpritez = -1
for i in range(0, enemyCount):
    enemy(50 + random.randint(3, 5000), 50 + random.randint(3, 5000), 40, 40, random.randint(1,4))
miniMap = miniMap() 
mainPlayer = player(screenSize[0]/2 - 100/2, screenSize[1]/2 - 91/2, 100, 91)
shots = 6
pause = button(100,100, "pause")
resume = button(screenSize[0]/2 - 120,screenSize[1]/2 - 100, "Resume")
sound = button(screenSize[0]/2 - 120,screenSize[1]/2, "Sound")
quit = button(screenSize[0]/2 - 120,screenSize[1]/2 + 100, "Quit")

while running:
    clock.tick(60)
    playerSprite = playerSpriteF
    fps = str(int(clock. get_fps()))
    pygame.display.set_caption(fps)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

            if shots > 0:
                shots -= 1
                shooting(mainPlayer.x, mainPlayer.y, pygame.mouse.get_pos())


    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        playerSprite = playerSpriteB
        if mainPlayer.y > -10:
            if checkCollision(mainPlayer.x + 50, mainPlayer.y + 65.5 - mainPlayer.speed, False) == True:
                if background.y < 0 + 10 or mainPlayer.y > screenSize[1]/2 - 91/2:
                    mainPlayer.y -= mainPlayer.speed
                else:
                    background.y -= mainPlayer.speed
                    for enemy in enemies:
                        enemy.y += mainPlayer.speed

    if keys[pygame.K_s]:
        playerSprite = playerSpriteF
        if mainPlayer.y < screenSize[1] - 100:
            if checkCollision(mainPlayer.x + 50,mainPlayer.y + 65.5 + mainPlayer.speed, False) == True:
                if (background.y - background.height + screenSize[1]) > 0 - 10 or mainPlayer.y != screenSize[1]/2 - 91/2:
                    mainPlayer.y += mainPlayer.speed
                else:
                    background.y += mainPlayer.speed
                    for enemy in enemies:
                        enemy.y -= mainPlayer.speed

    if keys[pygame.K_d]:
        playerSprite = playerSpriteR
        if mainPlayer.x < screenSize[0] - 100 + 30:
            if checkCollision(mainPlayer.x + 50 + mainPlayer.speed, mainPlayer.y + 65.5, False) == True:
                if (background.x - background.height + screenSize[0]) > 0 - 10 or mainPlayer.x != screenSize[0]/2 - 100/2:
                    mainPlayer.x += mainPlayer.speed
                else:
                    background.x += mainPlayer.speed
                    for enemy in enemies:
                        enemy.x -= mainPlayer.speed

    if keys[pygame.K_a]:
        playerSprite = playerSpriteL
        if mainPlayer.x > -20:
            if checkCollision(mainPlayer.x + 50 - mainPlayer.speed, mainPlayer.y + 65.5, False) == True:
                if background.x < 0 + 10 or mainPlayer.x != screenSize[0]/2 - 100/2:
                    mainPlayer.x -= mainPlayer.speed
                else:
                    background.x -= mainPlayer.speed
                    for enemy in enemies:
                        enemy.x += mainPlayer.speed
    if keys[pygame.K_r]:
        Reload = True



        
        
    reDraw(playerSprite)

pygame.quit()