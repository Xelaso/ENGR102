# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Alex So
#               Garret Sumpter
#               Zane Aschenback
#               Clint Smith
# Section:      573
# Assignment:   Lab Topic 12 Team
# Date:         11-9-2024
#

# As a team, we have gone through all required sections of the
# tutorial, and each team member understands the material


import numpy as np
import matplotlib.pyplot as plt
from math import *
x = np.linspace(-2, 2)
y = x ** 2 / (4*2)
fig, ax = plt.subplots()
ax.plot(x, y, color="red", linewidth = 2)
y = x ** 2 / (4*6)
ax.plot(x, y, color="blue", linewidth = 6)
plt.show()

x = np.linspace(-4, 4, 25)
y = 2*x**3 + 3*x**2 - 11*x - 6
fig, ax = plt.subplots()
ax.plot(x, y, color="yellow", marker='*', linewidth = 0, markeredgecolor = "black", markersize = 10)
plt.show()

x = np.linspace(-2 * pi, 2 * pi)
y2 = np.sin(x)
y1 = np.cos(x)

fig, ax = plt.subplots(2, 1, figsize=(10, 4))
fig.suptitle("Plot of cos(x) and sin(x)")
ax[0].plot(x, y1, label='sin(x)', color='b')
ax[0].legend()
ax[0].set_ylabel("y = cos(x)")
ax[0].grid(True)
ax[1].plot(x, y2, label='cos(x)', color='r')
ax[1].legend()
ax[1].set_ylabel("y = sin(x)")
ax[1].set_xlabel("x")
ax[1].grid(True)
plt.show()