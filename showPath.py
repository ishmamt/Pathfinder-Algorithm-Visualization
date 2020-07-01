# this script highlights the path that was found

# color
PATH = (255, 255, 51)
RED = (255, 0, 0)


def showpath(node):
    if node.prev is None:
        return
    showpath(node.prev)
    if node.col != RED:
        node.col = PATH
