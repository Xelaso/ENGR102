# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Alex So
#               Garret Sumpter
#               Zane Aschenback
#               Clint Smith
# Section:      573
# Assignment:   Lab 3.18 Still More Linear Interpolation
# Date:         3/9/2024
#

import math

#calculates the point
def calcPoint(p1, p2, t1, t2, tA):
    num = ((p2 - p1)/(t2-t1)) * (tA - t1) + p1
    return num

#retrieves user input
t1 = float(input("Enter time 1: "))
x1 = float(input("\nEnter the x position of the object at time 1: "))
y1 = float(input("\nEnter the y position of the object at time 1: "))
z1 = float(input("\nEnter the z position of the object at time 1: "))

t2 = float(input("\nEnter time 2: "))
x2 = float(input("\nEnter the x position of the object at time 2: "))
y2 = float(input("\nEnter the y position of the object at time 2: "))
z2 = float(input("\nEnter the z position of the object at time 2: "))


tA = t1
increment = (t2-t1)/4

#loops thru all 5
for i in range(5):
    xPos = calcPoint(x1, x2, t1, t2, tA)
    yPos = calcPoint(y1, y2, t1, t2, tA)
    zPos = calcPoint(z1, z2, t1, t2, tA)
    print('At time %.2f seconds the object is at (%.3f, %.3f, %.3f)' %(tA, xPos, yPos, zPos))
    tA += increment
    
