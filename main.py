# this script contains the main loop


# imports
from classdef import Node
from classdef import Grid
import pygame


# constants

# screen resolution
WIDTH = 700
HEIGHT = 700

# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# creating the grid
mainGrid = Grid(round(WIDTH * 0.25), 0, WIDTH - round(WIDTH * 0.25), HEIGHT, 100)


# functions
def redraw():
    win.fill(BLACK)  # fills the window after each frame
    pygame.draw.rect(win, WHITE, (0, 0, round(WIDTH * 0.25), HEIGHT))  # draws frame for holding the options
    pygame.draw.rect(win, RED, mainGrid.getGridPos())  # draws frame for the node grid
    pygame.display.update()


# pygaame window
pygame.init()  # pygame window init
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pathfinder Visualization')
clk = pygame.time.Clock()
FPS = 60  # frames per second
run = True  # for controlling the main loop

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# anyting between the lines are in the main loop
while run:
    clk.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False  # stop the game if user tries to quit
    redraw()
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

pygame.quit()
