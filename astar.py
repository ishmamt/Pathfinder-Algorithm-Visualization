# script for A* algorithm


# colors
CLOSED = (215, 215, 193)


def aStar(mainGrid):
    # first check to see if the open list is empty, meaning no possible solution
    if len(mainGrid.open) < 1:
        return True  # we have not found a path so we should stop the viz
    mainGrid.open.sort(key=lambda node: node.fcost)  # sorting to find the lowest fcost
    current = mainGrid.open[0]
    if current == mainGrid.end:
        return True
    current.getNeighbours(mainGrid)
    for neighbour in current.neighbours:
        if neighbour not in mainGrid.open:
            mainGrid.open.append(neighbour)
            neighbour.gcost = current.calcGcost()
            neighbour.hcost = neighbour.calcHcost(mainGrid.end)
            neighbour.fcost = neighbour.gcost + neighbour.hcost
            neighbour.prev = current
        else:
            if neighbour.fcost > current.calcGcost() + neighbour.calcHcost(mainGrid.end):
                neighbour.fcost = current.calcGcost() + neighbour.calcHcost(mainGrid.end)
                neighbour.prev = current
    mainGrid.open.remove(current)
    mainGrid.closed.append(current)
    if current != mainGrid.start:
        current.col = CLOSED
