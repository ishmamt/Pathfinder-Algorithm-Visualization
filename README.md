# Pathfinder Algorithm Visualization

This project is made to understand how popular pathfinding algorithms work. Currently it can visualize:
- Dijkstra's Algorithm
- A* Algorithm
- Best First Search Algorithm

It has a grid based system for drawing walls, placing starting and ending nodes or even generating a random maze.

## Requirements

- Install **Python**. I have used Python 3.8.1 but any version after Pyhton 3.5 would work. Download the latest version of Python from [here]('https://www.python.org/downloads/').

- Install **Pygame** library using pip. Use any command shell and use the following command:
    > ```pip install pygame```

- If for some reason **Tkinter** is not installed in your system (usually it comes with Python). Use any command shell and use the following command:
    > ```pip install pygame```

#### How to run it?

Compile and run  ```main.py```.

## Features

- A basic GUI that lets the user choose an algorithm, number of nodes in the grid and the speed of the visualization.

    ![The GUI implemented in the program to take user input](/screenshots/gui.jpg =200x)

    User can choose one of three pathfinding algorithms.

    ![Dropdown for algorithm selection](/screenshots/dropdown.jpg "Selecting an algorithm to view" =200x)

- It also provides a grid system where the user can:
    > - Draw walls.
    > - Draw start and end nodes.
    > - Erase walls or start/end node.
    > - Clear the grid
    > - Generate random maze

    ![The grid system](/screenshots/grid.jpg "Grid system" =300x)

    Drawing in the window is simplified for easier usage and intuitive.

    ![Drawing in the grid](/screenshots/draw.jpg "Drawing" =300x)

- The random maze generator randomly creates walls and paths. Usually the results are underwhelming as it's just random noise.
    ![Result of random maze generation](/screenshots/maze.jpg "Random maze" =300x)

- The path is highlighted if it is found.
    ![Path from start to end](/screenshots/path.jpg "Path shown from start to end" =300x)

## Future Plans

I plan to implement better visualization measures to make it interactable in real-time. An online version of this would be nice as it would require no installations.

### Made By
<small>&copy; [sed_cat]('https://github.com/ishmamt')  |  2020</small>
