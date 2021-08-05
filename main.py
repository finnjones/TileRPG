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
enemySprite = [pygame.image.load(FlexyPath + "/Sprites/Mobs/Cactus/tile011.png"), pygame.image.load(FlexyPath + "/Sprites/Mobs/Cactus/tile012.png"), pygame.image.load(FlexyPath + "/Sprites/Mobs/Cactus/tile013.png"), pygame.image.load(FlexyPath + "/Sprites/Mobs/Cactus/tile014.png"), pygame.image.load(FlexyPath + "/Sprites/Mobs/Cactus/tile015.png"), pygame.image.load(FlexyPath + "/Sprites/Mobs/Cactus/tile016.png"), pygame.image.load(FlexyPath + "/Sprites/Mobs/Cactus/tile017.png"), pygame.image.load(FlexyPath + "/Sprites/Mobs/Cactus/tile018.png"), pygame.image.load(FlexyPath + "/Sprites/Mobs/Cactus/tile019.png"), pygame.image.load(FlexyPath + "/Sprites/Mobs/Cactus/tile0020.png")]

playerSprite = pygame.image.load(FlexyPath + "/player.png")
bg = pygame.image.load(FlexyPath + "/map.jpg")

class player(object):
    def __init__(self, x, y, width, height):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.speed = 10

    def draw(self, window):
        window.blit(playerSprite, (self.x, self.y))
        
class enemy(object):
    def __init__(self, x, y, width, height):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
    def draw(self, window):
        window.blit(enemySprite, (self.x, self.y))
        

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
    pygame.display.flip()

running = True

bgCam = background(0, 0, 10280, 7019)
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

    if keys[pygame.K_s]:

        if (bgCam.y - bgCam.height + screenSize[1]) > 0 or mainPlayer.y != screenSize[1]/2 - 91/2:
            mainPlayer.y += mainPlayer.speed
        else:
            bgCam.y += mainPlayer.speed

    if keys[pygame.K_d]:
        if (bgCam.x - bgCam.height + screenSize[0]) > 0 or mainPlayer.x != screenSize[0]/2 - 100/2:
            mainPlayer.x += mainPlayer.speed
        else:
            bgCam.x += mainPlayer.speed

    if keys[pygame.K_a]:
        if bgCam.x < 0 + 10 or mainPlayer.x != screenSize[0]/2 - 100/2:
            mainPlayer.x -= mainPlayer.speed
        else:
            bgCam.x -= mainPlayer.speed
    reDraw()
pygame.quit()