import pygame, os
pygame.init()

black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 128, 0)
brown = (139,69,19)
red = (255, 0, 0)

clock = pygame.time.Clock()

NWQuadrant = [[0, 7, 1750, 1288], [259, 1323, 763, 273], [182, 1596, 119, 161], [665, 2177, 98, 70], [1036, 2261, 105, 63], [469, 2534, 112, 84], [574, 2835, 182, 126], [280, 3010, 105, 70], [301, 3381, 77, 63], [1211, 3171, 112, 91], [1862, 3122, 847, 329], [2345, 3010, 98, 63], [2422, 2422, 126, 84], [2891, 2618, 112, 91], [3451, 2359, 224, 168], [2905, 1785, 105, 70], [3262, 861, 203, 140], [3360, 581, 105, 77], [2800, 560, 126, 98], [2695, 777, 119, 70], [1974, 546, 182, 112], [2345, 210, 105, 84]]
SWQuadrant = [[1862, 3122, 861, 336], [553, 3626, 133, 119], [2331, 3479, 112, 77], [3073, 3521, 140, 119], [3458, 4137, 189, 126], [3269, 4473, 119, 91], [1127, 4193, 140, 119], [273, 4207, 126, 182], [14, 4557, 1288, 98], [1232, 4417, 77, 133], [1680, 4417, 105, 224], [1792, 4564, 2289, 98], [252, 4753, 903, 672], [105, 5411, 1309, 287], [1603, 5411, 2149, 280], [1638, 4753, 1918, 679], [3570, 5250, 168, 161], [3360, 5719, 364, 245], [3759, 5817, 147, 133], [273, 5782, 581, 840], [112, 6608, 2604, 280], [1750, 5922, 1169, 658], [2072, 5803, 560, 133], [2723, 6692, 441, 280], [3185, 6153, 560, 651]]
NEQuadrant = [[3647, 28, 49, 987], [3262, 889, 182, 119], [3451, 2352, 210, 175], [3647, 21, 56, 1008], [3633, 14, 3353, 91], [6965, 105, 28, 1925], [3647, 1967, 3339, 84], [3465, 2359, 189, 154], [4487, 2163, 91, 84], [3976, 2289, 3010, 847], [3710, 2835, 3283, 868], [4081, 3479, 2905, 553], [4368, 3640, 2625, 525], [4837, 4004, 2142, 539], [5173, 4445, 1799, 469], [3794, 1323, 616, 420], [4543, 1344, 602, 406], [5474, 1330, 602, 406], [6202, 1316, 616, 448], [3843, 1743, 7, 14], [3913, 1218, 420, 56], [4669, 1197, 406, 77], [5572, 1197, 448, 84], [6328, 1197, 441, 84], [5684, 245, 1106, 469], [4774, 294, 819, 525], [4109, 105, 567, 826], [5250, 812, 343, 259], [4123, 98, 2821, 175]]
SEQuadrant = [[4102, 3619, 2863, 910], [4753, 4123, 2212, 784], [5047, 4970, 126, 119], [4662, 5425, 98, 42], [5040, 5523, 91, 70], [5768, 5131, 140, 105], [5978, 5544, 189, 140], [4767, 6251, 203, 147], [4676, 6615, 2310, 364], [4942, 6286, 2030, 679], [5390, 5943, 1582, 644], [5922, 5523, 1050, 1106], [3577, 4529, 511, 126], [4032, 4669, 63, 2219], [3563, 5278, 168, 105], [3843, 5509, 84, 84], [3745, 5817, 182, 105], [3332, 5705, 392, 238]]


FlexyPath = os.path.dirname(os.path.abspath(__file__))
screenSize = (1620, 1000)
window = pygame.display.set_mode(screenSize)

playerSprite = pygame.image.load(FlexyPath + "/player.png")
bg = pygame.image.load(FlexyPath + "/map.png")

objectList = [
    [300, 225, 40, 44]]

class player(object):
    
    def __init__(self, x, y, width, height):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.speed = 3

    def draw(self, window):
        window.blit(playerSprite, (self.x, self.y))
        

        

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

def checkCollision(xPos, yPos):
    for i in range(0, len(objectList)):
        if xPos > objectList[i][0] and xPos < objectList[i][0] + objectList[i][2] or xPos + mainPlayer.width/2 > objectList[i][0] and xPos + mainPlayer.width/2 < objectList[i][0] + objectList[i][2]:
            if yPos > objectList[i][1] and yPos < objectList[i][1] + objectList[i][3] or yPos +  mainPlayer.height/2 > objectList[i][1] and yPos + mainPlayer.height/2 < objectList[i][1] + objectList[i][3]:
                return False
    return True

running = True

bgCam = background(0, 0, 640, 640)
mainPlayer = player(screenSize[0]/2 - 30/2, screenSize[1]/2 - 30/2, 30, 30)
while running:
    clock.tick(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        if checkCollision(mainPlayer.x - mainPlayer.speed, mainPlayer.y - mainPlayer.speed) == True:
            mainPlayer.y -= mainPlayer.speed

    if keys[pygame.K_s]:
        if checkCollision(mainPlayer.x + mainPlayer.speed, mainPlayer.y + mainPlayer.speed) == True:
            mainPlayer.y += mainPlayer.speed

    if keys[pygame.K_d]:
        if checkCollision(mainPlayer.x + mainPlayer.speed, mainPlayer.y + mainPlayer.speed) == True:
            mainPlayer.x += mainPlayer.speed

    if keys[pygame.K_a]:
        if checkCollision(mainPlayer.x - mainPlayer.speed, mainPlayer.y - mainPlayer.speed) == True:
            mainPlayer.x -= mainPlayer.speed

    reDraw()
pygame.quit()