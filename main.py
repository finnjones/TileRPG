import pygame, os
pygame.init()

black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 128, 0)
brown = (139,69,19)
red = (255, 0, 0)

clock = pygame.time.Clock()


FlexyPath = os.path.dirname(os.path.abspath(__file__))
screenSize = (1620 , 1000)
window = pygame.display.set_mode(screenSize)
enemySpriteNsc = [pygame.image.load(FlexyPath + "/Sprites/Mobs/Cactus/tile011.png"), pygame.image.load(FlexyPath + "/Sprites/Mobs/Cactus/tile012.png"), pygame.image.load(FlexyPath + "/Sprites/Mobs/Cactus/tile013.png"), pygame.image.load(FlexyPath + "/Sprites/Mobs/Cactus/tile014.png"), pygame.image.load(FlexyPath + "/Sprites/Mobs/Cactus/tile015.png"), pygame.image.load(FlexyPath + "/Sprites/Mobs/Cactus/tile016.png"), pygame.image.load(FlexyPath + "/Sprites/Mobs/Cactus/tile017.png"), pygame.image.load(FlexyPath + "/Sprites/Mobs/Cactus/tile018.png"), pygame.image.load(FlexyPath + "/Sprites/Mobs/Cactus/tile019.png"), pygame.image.load(FlexyPath + "/Sprites/Mobs/Cactus/tile020.png")]
playerSpriteNsc = [pygame.image.load(FlexyPath + "/Sprites/Player/tile014.png"), pygame.image.load(FlexyPath + "/Sprites/Player/tile015.png"), pygame.image.load(FlexyPath + "/Sprites/Player/tile016.png"), pygame.image.load(FlexyPath + "/Sprites/Player/tile017.png"), pygame.image.load(FlexyPath + "/Sprites/Player/tile018.png"), pygame.image.load(FlexyPath + "/Sprites/Player/tile019.png"), pygame.image.load(FlexyPath + "/Sprites/Player/tile020.png"), pygame.image.load(FlexyPath + "/Sprites/Player/tile021.png")]
enemySprite = []
playerSprite = []
for i in enemySpriteNsc:
    i = pygame.transform.scale(i, (100, 100))
    enemySprite.append(i)
for i in playerSpriteNsc:
    i = pygame.transform.scale(i, (100, 100))
    playerSprite.append(i)

# playerSprite = pygame.image.load(FlexyPath + "/player.png")
bg = pygame.image.load(FlexyPath + "/map.jpg")

class player(object):
    def __init__(self, x, y, width, height):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.speed = 10
        self.changeSprite = 0
    def draw(self, window):
        if self.changeSprite > 38:
            self.changeSprite = -1
        self.changeSprite += 1
        window.blit(playerSprite[self.changeSprite//5], (self.x, self.y))

        
class enemy(object):
    def __init__(self, x, y, width, height):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.changeSprite = 0
    def draw(self, window):
        if self.changeSprite > 48:
            self.changeSprite = -1
        self.changeSprite += 1
        window.blit(enemySprite[self.changeSprite//5], (self.x, self.y))

        

class background(object):
    def __init__(self, x, y, width, height):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
    def draw(self, window):
        window.blit(bg, (0 - self.x, 0 - self.y))

def reDraw():
    bgCam.draw(window)
    mainPlayer.draw(window)
    bad1.draw(window)
    pygame.display.flip()

running = True

bgCam = background(0, 0, 10280, 7019)
bad1 = enemy(100, 100, 40, 40)
mainPlayer = player(screenSize[0]/2 - 100/2, screenSize[1]/2 - 91/2, 100, 91)
while running:
    clock.tick(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        if bgCam.y < 0 + 10 or mainPlayer.y > screenSize[1]/2 - 91/2:
            mainPlayer.y -= mainPlayer.speed
        else:
            bgCam.y -= mainPlayer.speed
            bad1.y += mainPlayer.speed

    if keys[pygame.K_s]:

        if (bgCam.y - bgCam.height + screenSize[1]) > 0 or mainPlayer.y != screenSize[1]/2 - 91/2:
            mainPlayer.y += mainPlayer.speed
        else:
            bgCam.y += mainPlayer.speed
            bad1.y -= mainPlayer.speed

    if keys[pygame.K_d]:
        if (bgCam.x - bgCam.height + screenSize[0]) > 0 or mainPlayer.x != screenSize[0]/2 - 100/2:
            mainPlayer.x += mainPlayer.speed
        else:
            bgCam.x += mainPlayer.speed
            bad1.x -= mainPlayer.speed

    if keys[pygame.K_a]:
        if bgCam.x < 0 + 10 or mainPlayer.x != screenSize[0]/2 - 100/2:
            mainPlayer.x -= mainPlayer.speed
        else:
            bgCam.x -= mainPlayer.speed
            bad1.x += mainPlayer.speed
    
    

    reDraw()
pygame.quit()