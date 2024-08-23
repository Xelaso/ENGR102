# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Alexander So
# Section:      573
# Assignment:   Lab 2 More Linear Interpolation
# Date:         22/8/2024
#

import math

#calculates the point
def calcPoint(p1, p2, t1, t2, tA):
    num = ((p2 - p1)/(t2-t1)) * (tA - t1) + p1
    return num

x1 = 8
y1 = 6
z1 = 7
t1 = 12

x2 = -5
y2 = 30
z2 = 9
t2 = 85

tA = 30.0

#loops thru all 5
for i in range(5):
    print('At time', tA, 'seconds:')
    print('x' + str(i + 1) + ' =', calcPoint(x1, x2, t1, t2, tA), 'm')
    print('y' + str(i + 1) + ' =', calcPoint(y1, y2, t1, t2, tA), 'm')
    print('z' + str(i + 1) + ' =', calcPoint(z1, z2, t1, t2, tA), 'm')
    tA += 7.5
    if(i != 4):
        print('-----------------------')
