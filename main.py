# this script contains the main loop


# imports
from classdef import Grid, Choice
from dijkstra import dijkstra
from astar import aStar
from bestfirst import bestFirst
from showPath import showpath
from gui import gui, notFound
import pygame


# constants

# screen resolution
WIDTH = 700
HEIGHT = 700

# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BG_COL = (0, 64, 128)


# functions

def redraw():
    win.fill(BLACK)  # fills the window after each frame
    pygame.draw.rect(win, BG_COL, (0, 0, round(WIDTH * 0.25), HEIGHT))  # draws frame for holding the options
    pygame.draw.rect(win, WHITE, mainGrid.getPos())  # draws frame for the node grid
    mainGrid.draw(win, buttonFont)
    pygame.display.update()


# user input
choice = Choice()
gui(choice)
delay = choice.speed
algorithms = [dijkstra, aStar, bestFirst]
pathfinder = algorithms[choice.algo]

# creating the grid
mainGrid = Grid((WIDTH // 4), 0, WIDTH - (WIDTH // 4), HEIGHT, choice.nodes)


# pygaame window
pygame.init()  # pygame window init
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pathfinder Visualization')
clk = pygame.time.Clock()
FPS = 60  # frames per second
buttonFont = pygame.font.SysFont('Microsoft YaHei Light', 25)  # button font
run = True  # for controlling the main loop

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# anyting between the lines are in the main loop
while run:
    clk.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False  # stop the game if user tries to quit
        if pygame.mouse.get_pressed()[0]:  # only detects left click
            mainGrid.clickOnGrid(pygame.mouse.get_pos())  # checks if the click happened on grid
    if mainGrid.vizStarted:
        if mainGrid.start not in mainGrid.open and mainGrid.start not in mainGrid.closed:
            mainGrid.open.append(mainGrid.start)  # append the start node to the open list
            mainGrid.start.hcost = mainGrid.start.calcHcost(mainGrid.end)
            mainGrid.start.fcost = mainGrid.start.gcost + mainGrid.start.hcost
        if pathfinder(mainGrid, delay):
            if len(mainGrid.open) < 1:
                print('No possible path.')  # path not found
                run = False
            else:
                showpath(mainGrid.end)  # draws the path it has found
    redraw()
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

if len(mainGrid.open) < 1:  # no valid path found
    notFound()
pygame.quit()
