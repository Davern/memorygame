import sys
import tkinter as tk
import random
import pygame



class Tile(object):
    blankImage = pygame.image.load('apple.jpg')
    def __init__(self, x, y, image, cover):
        self.image = image
        self.cover = cover
        self.covered = True
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.x = x
        self.y = y

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

class Game():
    def __init__(self):
        pass

    def draw(self):
        pass

    def handleMouseClick():
        pass

    def checkGameStatus():
        pass

def main():
    global size
    size = 600
    pygame.init()
    window = pygame.display.set_mode((size,size))
    pygame.display.set_caption('Memory Challenge')
    flag = True
    apple_image = pygame.image.load('apple.jpg')
    orange_image = pygame.image.load('orange.jpg')
    banana_image = pygame.image.load('banana.jpg')

    clock = pygame.time.Clock()


    while flag:
        pygame.time.delay(50)
        clock.tick(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        redrawWindow(window)

main()
