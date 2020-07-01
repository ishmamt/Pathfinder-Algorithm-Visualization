# script for dijkstra's algorithm

# imports
# from classdef import Node, Grid

# colors
CLOSED = (215, 215, 193)


def dijkstra(mainGrid):
    # first check to see if the open list is empty, meaning no possible solution
    if len(mainGrid.open) < 1:
        return True  # we have not found a path so we should stop the viz
    mainGrid.open.sort(key=lambda node: node.gcost)  # sorting to find the lowest gcost node
    current = mainGrid.open[0]
    if current == mainGrid.end:
        return True
    current.getNeighbours(mainGrid)
    for neighbour in current.neighbours:
        if neighbour not in mainGrid.open:
            mainGrid.open.append(neighbour)
        if neighbour.gcost > current.calcGcost():
            neighbour.gcost = current.calcGcost()
            neighbour.prev = current
    mainGrid.open.remove(current)
    mainGrid.closed.append(current)
    current.col = CLOSED
