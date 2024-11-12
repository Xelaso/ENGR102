# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Alexander So
# Section:      573
# Assignment:   Lab Topic 12 Individual
# Date: 11-9-2024        
#
import numpy as np
import matplotlib.pyplot as plt

point = np.array([[0], [1]])
matrix = np.array([[1.02, 0.095], [-0.095, 1.02]])
pointsArr = []
pointsArr.append(point)
for i in range(250):
    newP = matrix @ pointsArr[i]
    pointsArr.append(newP)

fig, ax = plt.subplots()
fig.suptitle("Pretty Plot")
ax.set_xlabel("X", color="black")
ax.set_ylabel("Y", color="black")
for p in pointsArr:
    x = p[0][0]
    y = p[1][0]
    ax.plot(x, y, 'ro')

plt.show()