import sys
import random
import pygame
import time
from tkinter import messagebox

count = 0

class Tile(object):
    blankImage = pygame.image.load('square-48.png')
    def __init__(self, tilePos, image, cover, id):
        self.image = image
        self.id = id
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

    def cover_tile(self):
        self.covered = True
        self.draw()

    def select(self, pos):
        global tileA, tileB, answer_list, count, answer_dict, gameCheck
        if self.covered and count < 2:
            
            mouseX = pos[0]
            mouseY = pos[1]

            if mouseX >= self.x and mouseX  <= self.x + self.width:
                if mouseY >= self.y and mouseY <= self.y + self.height:
                    self.draw(self.image)
                    self.covered = False
                    answer_list.append(self.id)
                    answer_dict[self] = self
                    count+=1
                    gameCheck+=1




class Game:
    boardSize = 4
    gap = 80
    def __init__(self, surface, images):
        self.gameOver = False
        self.surface = surface
        self.images = images
        tileWidth = images[0][0].get_width()
        tileHeight = images[0][0].get_height()

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
                
                tile = Tile(tilePos,image[0],surface, image[1])

                rows.append(tile)

            self.board.append(rows)

    def draw(self):
        for row in self.board:
            for tile in row:
                tile.draw()
        
        pygame.display.flip()

    def handleMouseClick(self, mousePos):
        global tileA, tileB, answer_list, count
        for row in self.board:
            for tile in row:
                tile.select(mousePos)
        
    def gameUpdate(self):
        global answer_list, count, answer_dict
        if (gameCheck == len(self.board)*len(self.board)):
            self.gameOver = True
        if not self.gameOver:
            pygame.draw.rect(self.surface, pygame.Color('Black'), (self.surface.get_width() - 50, 0, 100, 100))
        else:
            ans = messagebox.askyesno("Game Completed!", "Do you wish to try again?")
            if (ans): 
                pygame.quit()
                main()
            else: 
                pygame.quit()
                sys.quit()
            
            

def main():
    global size, tileA, tileB, answer_list, count, answer_dict, gameCheck
    size = 600
    pygame.init()
    tileA = None
    tileB = None
    answer_list = []
    answer_dict = {}
    count = 0
    gameCheck = 0
    window = pygame.display.set_mode((size,size))
    pygame.display.set_caption('Memory Challenge')
    flag = True
    images = []
    i = 0
    imageTitles = ["apple.png", "orange.png", "banana.png", "grape.png", "peach.png", "cherry.png", "blueberry.png", "raspberry.png"]
    for title in imageTitles:
        image = pygame.image.load(title)
        temp = [image, i]
        images.append(temp)
        images.append(temp)
        i +=1


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
        if len(answer_list) == 2:
            time.sleep(1)
            if (answer_list[0] == answer_list[1]): 
                print("Match!")
                answer_list = []
                answer_dict = {}
                count = 0
            else: 
                print("No Match!")
                answer_list = []
                count = 0
                for img in answer_dict:
                    img.cover_tile()
                gameCheck -= 2
                answer_dict = {}
            instance.gameUpdate()
            pygame.display.update()

main()
