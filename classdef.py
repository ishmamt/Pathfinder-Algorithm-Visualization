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
        # self.start = False
        # self.end = False
        self.neighbours = list()  # list of all the neighbours
        self.gcost = 10000000000  # any high value ie. infinity
        self.hcost = None  # heuristic cost
        self.fcost = None  # addition of gcost & hcost
        self.prev = None  # this represents the parent node that has to be traversed to get to this node

    def setStart(self):
        self.col = GREEN
        self.gcost = 0

    def setEnd(self):
        self.col = RED
        self.hcost = 0

    def setWall(self):
        if self.col == WHITE:
            self.col = BLACK

    def clear(self):
        # resets a node
        self.col = WHITE
        self.gcost = 10000000000
        self.hcost = None
        self.fcost = None

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

        # grid modes
        self.drawingWalls = True  # toggle for if the user is drawing walls
        self.drawingStart = False  # toggle for if the user is drawing start node
        self.drawingEnd = False  # toggle for if the user is drawing end node
        self.drawingErase = False  # toggle for if the user is erasing walls
        self.vizStarted = False  # toggle for if the visualization has already started

        self.nodeDim = self.width // self.num  # dimentions of each node
        self.grid = self.createGrid()

        # creating the buttons
        self.setStartButton = pygame.Rect(10, 10, 150, 40)
        self.setEndButton = pygame.Rect(10, 90, 150, 40)
        self.setWallButton = pygame.Rect(10, 170, 150, 40)
        self.setEraseButton = pygame.Rect(10, 250, 150, 40)
        self.randMazeButton = pygame.Rect(10, 330, 150, 40)
        self.clearButton = pygame.Rect(10, 410, 150, 40)
        self.startVizButton = pygame.Rect(10, 530, 150, 60)

        # for keeping track of the start and end
        self.start = None
        self.end = None

    def createGrid(self):
        return [[Node((col * self.nodeDim) + self.x, (row * self.nodeDim) + self.y, self.nodeDim) for col in range(self.num)] for row in range(self.height // self.nodeDim)]  # returns a grid based on the number of nodes

    def makeRandMaze(self):
        # makes a random maze
        pass

    def getPos(self):
        return (self.x, self.y, self.width, self.height)  # returns the dimentions of the whole grid

    def draw(self, win):
        for row in range(self.height // self.nodeDim):
            for col in range(self.num):
                self.grid[row][col].draw(win)
        self.drawButtons(win)  # draws the buttons

    def drawButtons(self, win):
        pygame.draw.rect(win, BLACK, self.setStartButton)  # drawing the start button
        pygame.draw.rect(win, BLACK, self.setEndButton)  # drawing the end button
        pygame.draw.rect(win, BLACK, self.setWallButton)  # drawing the wall button
        pygame.draw.rect(win, BLACK, self.setEraseButton)  # drawing the erase button
        pygame.draw.rect(win, BLACK, self.randMazeButton)  # drawing the random maze button
        pygame.draw.rect(win, BLACK, self.clearButton)  # drawing the clear grid button
        pygame.draw.rect(win, BLACK, self.startVizButton)  # drawing the startviz button

    def clickOnGrid(self, mousePos):
        if mousePos[1] // self.nodeDim >= len(self.grid) or (mousePos[0] - self.x) // self.nodeDim >= len(self.grid[0]):  # to stay in bounds of the grid list
            return
        if mousePos[0] < self.x:  # checking if the click is done on the grid
            return
        node = self.getGridPos(mousePos)
        # approaching according to the grid state
        if self.drawingStart:
            if self.start is not None:
                self.start.clear()  # clears if another node for the same purpose exists
            node.setStart()
            self.start = node
        elif self.drawingEnd:
            if self.end is not None:
                self.end.clear()  # clears if another node for the same purpose exists
            node.setEnd()
            self.end = node
        elif self.drawingWalls:
            node.setWall()

    def getGridPos(self, mousePos):
        # this translates the mouse click to a node in the array
        return self.grid[mousePos[1] // self.nodeDim][(mousePos[0] - self.x) // self.nodeDim]
