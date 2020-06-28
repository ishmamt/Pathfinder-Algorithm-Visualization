# Script for all the classes

# imports
import pygame


# constants
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)


class Node(object):
    # class definition for the nodes
    def __init__(self, x=0, y=0, width=0, height=0):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
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

    def getfcost(self):
        return self.gcost + self.hcost

    def getNeighbours(self, grid):
        for row in range(-1, 2):
            for col in range(-1, 2):
                print(row, col)

    def draw(self):
        pass


class Grid(object):
    # class definition for the grid
    def __init__(self, x, y, num):
        self.x = x  # x, y is the position of the first node in grid
        self.y = y
        self.num = num  # number on nodes in grid. It dictates the width of the nodes
        self.grid = self.createGrid()

    def createGrid(self):
        return [[Node() for col in range(self.num)] for row in range(self.num)]  # returns a grid based on the number of nodes

    def makeRandMaze(self):
        # makes a random maze
        pass
