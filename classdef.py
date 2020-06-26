# Script for all the classes

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
        self.hcost = None  # we don't know yet
        self.fcost = None
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

    def getNeighbours(self):
        for row in range(-1, 2):
            for col in range(-1, 2):
                print(row, col)


# class Grid(object):
#     # class definition for the grid
#     def __init__(self, rows, cols):
#         self.rows = rows
#         self.cols = cols
#         # creating the list of nodes in grid
