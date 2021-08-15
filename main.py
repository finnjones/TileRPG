import pygame, os, math, numpy as np

pygame.init()

black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 128, 0)
brown = (139,69,19)
red = (255, 0, 0)

clock = pygame.time.Clock()
vec = pygame.math.Vector2


FlexyPath = os.path.dirname(os.path.abspath(__file__))
screenSize = (1620 , 1000)

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

enemySprite = []
enemySpriteF = []
enemySpriteR = []
enemySpriteL = []
enemySpriteB = []

playerSpriteF = []
playerSpriteR = []
playerSpriteL = []
playerSpriteB = []

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
        
        self.changeSprite = 0
    def draw(self, window, playerSpriteR):
        
        self.pos = vec(self.x, self.y)
        if self.changeSprite > 38:
            self.changeSprite = -1
        self.changeSprite += 1
        window.blit(playerSpriteR[self.changeSprite//5], (self.x, self.y))

        
class enemy(object):
    def __init__(self, x, y, width, height):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.changeSprite = 0
        self.rot = 0
    def draw(self, window):
        self.pos = vec(self.x, self.y)
        self.rot = (mainPlayer.pos - self.pos).angle_to(vec(1, 0))
        if self.rot < 0:
            self.rot += 360
        # print(self.changeSprite)
        # print(self.rot)
        enemySprite = enemySpriteF

        if self.rot >= 225 and self.rot <= 315:
            enemySprite = enemySpriteF
        if self.rot >= 45 and self.rot <= 135:
            enemySprite = enemySpriteB
        if self.rot > 135 and self.rot < 225:
            enemySprite = enemySpriteL
        if self.rot < 45 or self.rot > 315:
            enemySprite = enemySpriteR


        if self.y < mainPlayer.y:
            self.y += 2
        if self.y > mainPlayer.y:
            self.y -= 2
        if self.x > mainPlayer.x:
            self.x -= 2
        if self.x < mainPlayer.x:
            self.x += 2
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
        pygame.draw.rect(window, red, pygame.Rect((mainPlayer.x + bgCam.x)/35 + self.x, (mainPlayer.y + bgCam.y)/35 + self.y, 3, 3))


class background(object):
    def __init__(self, x, y, width, height):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
    def draw(self, window):
        window.blit(bg, (0 - self.x, 0 - self.y))

def reDraw(playerS):
    bgCam.draw(window)
    mainPlayer.draw(window, playerS)
    bad1.draw(window)
    miniMap.draw(window)
    pygame.display.flip()

running = True

bgCam = background(0, 0, 7000, 7000)
bad1 = enemy(500, 500, 40, 40)
miniMap = miniMap() 
mainPlayer = player(screenSize[0]/2 - 100/2, screenSize[1]/2 - 91/2, 100, 91)

while running:
    clock.tick(100)
    playerSprite = playerSpriteF
    fps = str(int(clock. get_fps()))
    pygame.display.set_caption(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        playerSprite = playerSpriteB
        if mainPlayer.y > -10:
            if bgCam.y < 0 + 10 or mainPlayer.y > screenSize[1]/2 - 91/2:
                mainPlayer.y -= mainPlayer.speed
            else:
                bgCam.y -= mainPlayer.speed
                bad1.y += mainPlayer.speed

    if keys[pygame.K_s]:
        playerSprite = playerSpriteF
        if mainPlayer.y < screenSize[1] - 100:
            if (bgCam.y - bgCam.height + screenSize[1]) > 0 - 10 or mainPlayer.y != screenSize[1]/2 - 91/2:
                mainPlayer.y += mainPlayer.speed
            else:
                bgCam.y += mainPlayer.speed
                bad1.y -= mainPlayer.speed

    if keys[pygame.K_d]:
        playerSprite = playerSpriteR
        if mainPlayer.x < screenSize[0] - 100 + 30:
            if (bgCam.x - bgCam.height + screenSize[0]) > 0 - 10 or mainPlayer.x != screenSize[0]/2 - 100/2:
                mainPlayer.x += mainPlayer.speed
            else:
                bgCam.x += mainPlayer.speed
                bad1.x -= mainPlayer.speed

    if keys[pygame.K_a]:
        playerSprite = playerSpriteL
        if mainPlayer.x > -20:
            if bgCam.x < 0 + 10 or mainPlayer.x != screenSize[0]/2 - 100/2:
                mainPlayer.x -= mainPlayer.speed
            else:
                bgCam.x -= mainPlayer.speed
                bad1.x += mainPlayer.speed

    reDraw(playerSprite)
pygame.quit()