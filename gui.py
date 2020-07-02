# this script contains the tkinter gui

# imports
import tkinter as tk

# constants
WIDTH = 500
HEIGHT = 400


# class Choice(object):
#     # class for getting the user choice
#     def __init__(self):
#         self.algo = None
#         self.nodes = None
#         self.speed = None


# gui elements
myfont = ('Microsoft YaHei Light', '15')  # font face and size
buttonfont = ('Microsoft YaHei Light', '10')
titlefont = ('Microsoft YaHei Light', '30')
BG_COL = '#004080'
algorithms = ["Dijkstra's Algorithm", "A* Algorithm", "Best First Search"]
number = [10, 20, 30, 40]
speed = ['Fast', 'Medium', 'Slow']


def draw(root, choice):
    # all the gui elemnts drawn here
    bg = tk.Label(root, bg=BG_COL)
    bg.place(relheight=1, relwidth=1)

    # title
    titleFrame = tk.Frame(root, bg=BG_COL)
    titleFrame.place(relwidth=1, relheight=0.15)

    title = tk.Label(titleFrame, bg=BG_COL, fg='white', text='Pathfinder Visualization', font=titlefont)
    title.place(relwidth=1, relheight=1)

    # frame to hold the selections
    selectframe = tk.Frame(root, bg=BG_COL)
    selectframe.place(relwidth=1, relheight=1 - 0.15, rely=0.2)

    # choosing the algorithm to visualize
    algoText = tk.Label(selectframe, bg=BG_COL, fg='white', text='Choose algorithm: ', font=myfont)
    algoText.place(relx=0.15)
    choiceAlgo = tk.StringVar()  # the user's choice of algorithm
    choiceAlgo.set(algorithms[0])
    drop = tk.OptionMenu(selectframe, choiceAlgo, *algorithms)
    drop.place(relx=0.5, relwidth=0.3, relheight=0.1)

    # choosing number of nodes
    nodeText = tk.Label(selectframe, bg=BG_COL, fg='white', text='Number of nodes in a row: ', font=myfont)
    nodeText.place(relx=0.15, rely=0.2)
    nodeNum = tk.IntVar()  # the number of nodes in a row
    nodeNum.set(number[0])
    numdrop = tk.OptionMenu(selectframe, nodeNum, *number)
    numdrop.place(relx=0.65, rely=0.2)

    # choosing speed of viz
    speedText = tk.Label(selectframe, bg=BG_COL, fg='white', text='Speed: ', font=myfont)
    speedText.place(relx=0.15, rely=0.4)
    speedChoice = tk.StringVar()
    speedChoice.set(speed[0])
    speeddrop = tk.OptionMenu(selectframe, speedChoice, *speed)
    speeddrop.place(relx=0.3, rely=0.4)

    # start button
    button = tk.Button(selectframe, text='Start', font=buttonfont, command=lambda: start(choice, root, speedChoice, nodeNum, choiceAlgo))
    button.place(relx=0.37, rely=0.7, relwidth=0.25)


def start(choice, root, speedChoice, nodeNum, choiceAlgo):
    # choice.speed = speedChoice.get()
    # choice.algo = choiceAlgo.get()
    choice.nodes = nodeNum.get()
    if speedChoice.get() == 'Fast':
        choice.speed = 0
    elif speedChoice.get() == 'Medium':
        choice.speed = 100
    else:
        choice.speed = 200
    if choiceAlgo.get() == "Dijkstra's Algorithm":
        choice.algo = 0
    elif choiceAlgo.get() == 'A* Algorithm':
        choice.algo = 1
    else:
        choice.algo = 2
    root.destroy()


def gui(choice):
    # .......the main GUI loop starts here.......
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # whatever is written between this is gonna be in the gui

    root = tk.Tk()  # creating a root as the main body of the GUI
    root.title('Pathfinder Visualization')

    # canvas to hold the shape of GUI by drawing a rectangle
    canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
    draw(root, choice)
    canvas.pack()
    root.mainloop()
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
