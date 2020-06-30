# script for all the classes
# this handles the drawing as well as the button presses for all the pygame window

# imports
import pygame
import random


# constants
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
INACTIVE_BUTTON = BLACK
ACTIVE_BUTTON = GREEN
BUTTON_TEXT_COL = WHITE


class Node(object):
    # class definition for the nodes
    def __init__(self, x=0, y=0, dim=0):
        self.x = x
        self.y = y
        self.dim = dim
        self.col = WHITE
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
        self.clearGrid()
        self.clearState()
        for row in range(len(self.grid)):
            for col in range(len(self.grid[0])):
                if bool(random.getrandbits(1)):
                    self.grid[row][col].setWall()

    def clearGrid(self):
        # clears the grid
        for row in range(len(self.grid)):
            for col in range(len(self.grid[0])):
                self.grid[row][col].clear()
        self.start = None
        self.end = None

    def getPos(self):
        return (self.x, self.y, self.width, self.height)  # returns the dimentions of the whole grid

    def draw(self, win, buttonFont):
        for row in range(self.height // self.nodeDim):
            for col in range(self.num):
                self.grid[row][col].draw(win)
        self.drawButtons(win, buttonFont)  # draws the buttons

    def drawButtons(self, win, buttonFont):
        if self.drawingStart:
            pygame.draw.rect(win, ACTIVE_BUTTON, self.setStartButton)  # drawing the start button
        else:
            pygame.draw.rect(win, INACTIVE_BUTTON, self.setStartButton)  # drawing the start button
        startButton = buttonFont.render('Draw start', 1, BUTTON_TEXT_COL)
        win.blit(startButton, (self.setStartButton.left + 30, self.setStartButton.top + 11))

        if self.drawingEnd:
            pygame.draw.rect(win, ACTIVE_BUTTON, self.setEndButton)  # drawing the end button
        else:
            pygame.draw.rect(win, INACTIVE_BUTTON, self.setEndButton)  # drawing the end button
        endButton = buttonFont.render('Draw end', 1, BUTTON_TEXT_COL)
        win.blit(endButton, (self.setEndButton.left + 35, self.setEndButton.top + 11))

        if self.drawingWalls:
            pygame.draw.rect(win, ACTIVE_BUTTON, self.setWallButton)  # drawing the wall button
        else:
            pygame.draw.rect(win, INACTIVE_BUTTON, self.setWallButton)  # drawing the wall button
        wallButton = buttonFont.render('Draw walls', 1, BUTTON_TEXT_COL)
        win.blit(wallButton, (self.setWallButton.left + 35, self.setWallButton.top + 11))

        if self.drawingErase:
            pygame.draw.rect(win, ACTIVE_BUTTON, self.setEraseButton)  # drawing the erase button
        else:
            pygame.draw.rect(win, INACTIVE_BUTTON, self.setEraseButton)  # drawing the erase button
        eraseButton = buttonFont.render('Erase', 1, BUTTON_TEXT_COL)
        win.blit(eraseButton, (self.setEraseButton.left + 52, self.setEraseButton.top + 11))

        pygame.draw.rect(win, INACTIVE_BUTTON, self.randMazeButton)  # drawing the random maze button
        mazeButton = buttonFont.render('Random maze', 1, BUTTON_TEXT_COL)
        win.blit(mazeButton, (self.randMazeButton.left + 15, self.randMazeButton.top + 11))

        pygame.draw.rect(win, INACTIVE_BUTTON, self.clearButton)  # drawing the clear grid button
        clearGridButton = buttonFont.render('Clear Grid', 1, BUTTON_TEXT_COL)
        win.blit(clearGridButton, (self.clearButton.left + 29, self.clearButton.top + 11))

        pygame.draw.rect(win, INACTIVE_BUTTON, self.startVizButton)  # drawing the startviz button
        vizButton = buttonFont.render('Start Viz', 1, BUTTON_TEXT_COL)
        win.blit(vizButton, (self.startVizButton.left + 35, self.startVizButton.top + 20))

    def clickOnGrid(self, mousePos):
        if mousePos[1] // self.nodeDim >= len(self.grid) or (mousePos[0] - self.x) // self.nodeDim >= len(self.grid[0]):  # to stay in bounds of the grid list
            return
        if mousePos[0] < self.x:  # checking if the click is done on the grid
            self.clickOnSidebar(mousePos)
            return
        if self.vizStarted:
            return  # cannot draw on screen if the viz has already started

        node = self.getGridPos(mousePos)
        # proceeding according to the grid state
        if self.drawingStart:
            if node.col == WHITE:
                if self.start is not None:
                    self.start.clear()  # clears if another node for the same purpose exists
                node.setStart()
                self.start = node
        elif self.drawingEnd:
            if node.col == WHITE:
                if self.end is not None:
                    self.end.clear()  # clears if another node for the same purpose exists
                node.setEnd()
                self.end = node
        elif self.drawingWalls:
            node.setWall()
        elif self.drawingErase:
            if node == self.start:
                self.start = None
            elif node == self.end:
                self.end = None
            node.clear()

    def getGridPos(self, mousePos):
        # this translates the mouse click to a node in the array
        return self.grid[mousePos[1] // self.nodeDim][(mousePos[0] - self.x) // self.nodeDim]

    def clickOnSidebar(self, mousePos):
        # checks which button from the sidebar has been pressed
        if self.buttonClick(mousePos, self.setStartButton):
            if not self.drawingStart and not self.vizStarted:
                self.clearState()
                self.drawingStart = True
        elif self.buttonClick(mousePos, self.setEndButton):
            if not self.drawingEnd and not self.vizStarted:
                self.clearState()
                self.drawingEnd = True
        elif self.buttonClick(mousePos, self.setWallButton):
            if not self.drawingWalls and not self.vizStarted:
                self.clearState()
                self.drawingWalls = True
        elif self.buttonClick(mousePos, self.setEraseButton):
            if not self.drawingErase and not self.vizStarted:
                self.clearState()
                self.drawingErase = True
        elif self.buttonClick(mousePos, self.randMazeButton) and not self.vizStarted:
            self.makeRandMaze()
        elif self.buttonClick(mousePos, self.clearButton) and not self.vizStarted:
            self.clearGrid()
            self.clearState()
            self.drawingWalls = True  # after clearing the grid ut seems natural to default to drawing walls
        elif self.buttonClick(mousePos, self.startVizButton) and not self.vizStarted:
            if not self.vizStarted:
                self.clearState()
                self.vizStarted = True  # we need to start the vizualization here

    def clearState(self):
        # clears the state of the grid
        self.drawingStart = False
        self.drawingEnd = False
        self.drawingWalls = False
        self.drawingErase = False

    def buttonClick(self, mousePos, button):
        # returns if a button has been pressed
        return (mousePos[0] >= button.left and mousePos[0] <= button.right) and (mousePos[1] >= button.top and mousePos[1] <= button.bottom)
