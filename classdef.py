# Script for all the classes

# imports
import pygame


# constants
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


class Node(object):
    # class definition for the nodes
    def __init__(self, x=0, y=0, dim=0):
        self.x = x
        self.y = y
        self.dim = dim
        self.col = WHITE
        self.start = False
        self.end = False
        self.neighbours = list()  # list of all the neighbours
        self.gcost = 10000000000  # any high value ie. infinity
        self.hcost = None  # heuristic cost
        self.fcost = None  # addition of gcost & hcost
        self.prev = None  # this represents the parent node that has to be traversed to get to this node

    def setStart(self):
        self.start = True
        self.col = GREEN
        self.gcost = 0

    def setEnd(self):
        self.end = True
        self.col = RED
        self.hcost = 0

    def setWall(self):
        self.col = BLACK

    def getfcost(self):
        return self.gcost + self.hcost

    def getNeighbours(self, mainGrid):
        for row in range(-1, 2):
            for col in range(-1, 2):
                print(row, col)

    def getNodePos(self):
        return (self.x, self.y, self.dim, self.dim)

    def draw(self, win):
        if self.col == WHITE:
            pygame.draw.rect(win, BLACK, self.getNodePos(), 1)  # we are drawing them as black to get the grid border effect
        else:
            pygame.draw.rect(win, self.col, self.getNodePos())


class Grid(object):
    # class definition for the grid
    def __init__(self, x, y, width, height, num):
        self.x = x  # x, y is the position of the first node in grid
        self.y = y
        self.width = width
        self.height = height
        self.num = num  # number on nodes in grid. It dictates the width of the nodes
        self.drawingWalls = True  # toggle for if the user is drawing walls
        self.drawingStart = False  # toggle for if the user is drawing start node
        self.drawingEnd = False  # toggle for if the user is drawing end node
        # self.speed = 0  # this indicates the delay which controls the speed of the visualization
        self.nodeDim = self.width // self.num  # dimentions of each node
        self.grid = self.createGrid()

    def createGrid(self):
        return [[Node((col * self.nodeDim) + self.x, (row * self.nodeDim) + self.y, self.nodeDim) for col in range(self.num)] for row in range(self.height // self.nodeDim)]  # returns a grid based on the number of nodes

    def makeRandMaze(self):
        # makes a random maze
        pass

    def getGridPos(self):
        return (self.x, self.y, self.width, self.height)  # returns the dimentions of the whole grid

    def draw(self, win):
        for row in range(self.height // self.nodeDim):
            for col in range(self.num):
                self.grid[row][col].draw(win)
