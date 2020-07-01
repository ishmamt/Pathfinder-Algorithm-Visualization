# this script highlights the path that was found

# color
PATH = (255, 255, 51)


def showpath(node):
    if node.prev is None:
        return
    showpath(node.prev)
    node.col = PATH
