import sys
import random
import pygame



class Tile(object):
    blankImage = pygame.image.load('whitesquare.png')
    def __init__(self, tilePos, image, cover):
        self.image = image
        self.cover = cover
        self.covered = True
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.x = tilePos[0]
        self.y = tilePos[1]
        self.width = tilePos[2]
        self.height = tilePos[3]

    def draw(self, image=blankImage):
        self.cover.blit(image, (self.x, self.y))

    def select(self, pos):
        if self.covered:
            
            mouseX = pos[0]
            mouseY = pos[1]

            if mouseX >= self.x and mouseX  <= self.x + self.width:
                if mouseY >= self.y and mouseY <= self.y + self.height:
                    self.draw(self.image)
                    self.covered = False

class Game:
    boardSize = 4
    gap = 80
    def __init__(self, surface, images):
        self.gameOver = False
        self.surface = surface
        self.images = images
        tileWidth = images[0].get_width()
        tileHeight = images[0].get_height()

        self.board = []
        for row in range(0, Game.boardSize):
            rows = []
            for column in range(0, Game.boardSize):
                x = ((column + 1)* Game.gap) + (column * tileWidth)
                y = ((row + 1) * Game.gap) + (row * tileHeight)
                tilePos = [x,y,tileWidth,tileHeight]

                imageIndex = random.randrange(0, len(self.images))
                image = self.images[imageIndex]
                self.images.remove(image)
                
                tile = Tile(tilePos,image,surface)

                rows.append(tile)

            self.board.append(rows)

    def draw(self):
        for row in self.board:
            for tile in row:
                tile.draw()
        
        pygame.display.flip()

    def handleMouseClick(self, mousePos):
        for row in self.board:
            for tile in row:
                tile.select(mousePos)

    def gameUpdate(self):
        if not self.gameOver:
            pygame.draw.rect(self.surface, pygame.Color('Black'), (self.surface.get_width() - 50, 0, 100, 100))

def main():
    global size
    size = 600
    pygame.init()
    window = pygame.display.set_mode((size,size))
    pygame.display.set_caption('Memory Challenge')
    flag = True
    images = []
    imageTitles = ["apple.png", "orange.png", "banana.png", "grape.png", "peach.png", "cherry.png", "blueberry.png", "raspberry.png"]
    for title in imageTitles:
        image = pygame.image.load(title)
        images.append(image)
        images.append(image)


    clock = pygame.time.Clock()

    instance = Game(window, images)
    instance.draw()
    pygame.display.update()


    while flag:
        pygame.time.delay(50)
        clock.tick(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                instance.handleMouseClick(event.pos)

        instance.gameUpdate()
        pygame.display.update()

main()
