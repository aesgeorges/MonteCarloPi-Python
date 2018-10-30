import random as rd
import numpy as np
import matplotlib as mlp
mlp.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.patches as patch
from matplotlib.animation import FuncAnimation

inside = 0
outside = 0
coords = []
# ----Plotting the circle and the rectangle-------
x = np.linspace(0, 1, 200)
y = np.sqrt((0.5 ** 2) - ((x - 0.5) ** 2)) + 0.5  # Upper half of circle
neg_y = -np.sqrt(0.5**2 - ((x - 0.5) ** 2)) + 0.5  # Lower half of circle
fig, ax = plt.subplots()
ax.plot(x, y, 'blue')
ax.plot(x, neg_y, 'blue')
rect = patch.Rectangle((0, 0), 1, 1, linewidth=1, fill=False)
ax.add_patch(rect)
ax.axis('equal')
ax.axis('off')

def update(i):
    global inside
    global outside
    x_rand = rd.random()  # Random x coordinate
    y_rand = rd.random()  # Random y coordinate
    if (x_rand - 0.5) ** 2 + (y_rand - 0.5) ** 2 < (0.5**2):  # If the (x,y) coordinate falls inside the circle
        h = ax.plot(x_rand, y_rand, 'ro', markersize=1)
        inside += 1
    else:
        h = ax.plot(x_rand, y_rand, 'go', markersize=1)
        outside += 1
    pi = 4 * (inside / (inside + outside))
    ax.set_title("$\pi$ = " + str(format(pi, '.7f')))  # Show 7 decimal places of Pi
    return h

animation = FuncAnimation(fig, update, interval=100, frames=100)
plt.show()
