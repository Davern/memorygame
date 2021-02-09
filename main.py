import sys
import tkinter as tk
import random
import pygame



class Tile(object):
    surface = None
    border_size = 3
    border_color = pygame.Color('black')
    def __init__(self, x, y, image, cover):
        self.image = image
        self.cover = cover
        self.covered = True
        width = self.image.get_width()
        height = self.image.get_height()

        self.rect = pygame.Rect(x,y,width,height)

    def draw(self):
        pygame.draw.rect(Tile.surface, Tile.border_color, self.rect, Tile.border_size)
        Tile.surface.blit(self.image, self.rect)
        if self.covered:
            Tile.surface.blit(self.cover, self.rect)

    def select(self, pos):
        pass


def drawWindow(window):
    pass

def redrawWindow(window):
    pass

def reset():
    pass

def main():
    global i, size
    size = 600
    pygame.init()
    window = pygame.display.set_mode((size,size))
    pygame.display.set_caption('Memory Challenge')
    flag = True

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
