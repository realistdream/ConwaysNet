# ConwaysNet

README 

*Overview*

This Python script, conwaysnet.py, is an implementation of Conway's Game of Life using the NetworkX library in combination with Matplotlib to visualize the simulation. Conway's Game of Life is a cellular automaton devised by the British mathematician John Horton Conway in 1970. It consists of a grid of cells that evolve across multiple iterations according to specific rules.

*Features*

 - Grid Setup: The grid is initialized as a 50x50 two-dimensional network where each node represents a cell that is either alive or dead.
 - Random Initialization: Each cell is randomly initialized to be alive (1) or dead (0).
 - Game Rules Implementation: 
 -- The program implements the classic rules of Conway's Game of Life:

   1. A live cell with fewer than two or more than three live neighbors dies.
   2. A dead cell with exactly three live neighbors becomes alive.

 - Visualization: The state of the grid is visualized using Matplotlib's FuncAnimation, showing the evolution of the grid over time.

*Dependencies*
 - Python 3.X
 - NetworkX
 - Matplotlib

*Installation*

Make sure you have Python installed on your system. You can install the required libraries via pip:

> bash pip install networkx matplotlib

*Usage*

To run the simulation, simply execute the script:

> bash python conwaysnet.py

*Output*

The script will open a Matplotlib window displaying the evolution of the game. The simulation runs for up to 1000 frames with a 50 milliseconds interval per frame.

*Explanation*

Board Initialization:

A grid of size 50x50 is created using NetworkX's grid_2d_graph.
Each cell (node) is randomly set to 'alive' or 'dead' using Python's random module.
Game Evolution:

The function apply_rules(G) iterates over each cell to calculate the next state based on the number of live neighbors, applying the rules of the game to produce a new grid state.

*Visualization*

The function animate(frame) updates the grid each frame. The grid is drawn using Matplotlib, with the color of each node representing its alive state.
