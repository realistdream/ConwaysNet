import networkx as nx
import matplotlib.pyplot as plt
import random

# Initialize the board
BOARD_SIZE = (50, 50)

# Create the network
G = nx.grid_2d_graph(*BOARD_SIZE)

# Randomly initialize the node states
for node in G.nodes:
    G.nodes[node]['alive'] = random.randint(0, 1)

# Define the rules of the game
def apply_rules(G):
    # Create a copy of the network to store the next generation
    new_G = G.copy()

    # Iterate over each node in the network
    for node in G.nodes:
        i, j = node
        alive = G.nodes[node]['alive']

        # Count the number of live neighbors
        live_neighbors = sum([G.nodes[neighbor]['alive'] for neighbor in G.neighbors(node)])

        # Apply the rules of the game
        if alive == 1 and (live_neighbors < 2 or live_neighbors > 3):
            new_G.nodes[node]['alive'] = 0
        elif alive == 0 and live_neighbors == 3:
            new_G.nodes[node]['alive'] = 1

    # Return the next generation
    return new_G

# Create a figure to display the simulation
fig = plt.figure()
plt.axis('off')

# Define the animation function
def animate(frame):
    global G
    G = apply_rules(G)
    plt.cla()
    nx.draw(G, node_size=10, pos={node: node for node in G.nodes}, node_color=[G.nodes[node]['alive'] for node in G.nodes], cmap='gray')

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=1000, interval=50)

# Show the animation
plt.show()
