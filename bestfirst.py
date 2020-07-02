# script for best first search


# colors
CLOSED = (215, 215, 193)


def bestFirst(mainGrid, delay):
    # first check to see if the open list is empty, meaning no possible solution
    if len(mainGrid.open) < 1:
        return True  # we have not found a path so we should stop the viz
    mainGrid.open.sort(key=lambda node: node.hcost)  # sorting to find the lowest hcost
    current = mainGrid.open[0]
    if current == mainGrid.end:
        return True
    current.getNeighbours(mainGrid, delay)
    for neighbour in current.neighbours:
        if neighbour not in mainGrid.open:
            mainGrid.open.append(neighbour)
            neighbour.hcost = neighbour.calcHcost(mainGrid.end)
            neighbour.prev = current
        else:
            if neighbour.hcost > neighbour.calcHcost(mainGrid.end):
                neighbour.hcost = neighbour.calcHcost(mainGrid.end)
                neighbour.prev = current
    mainGrid.open.remove(current)
    mainGrid.closed.append(current)
    if current != mainGrid.start:
        current.col = CLOSED
