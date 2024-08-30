# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Alex So
#               Zane Aschenback
#               Garett Sumpter
#               Clint Smith
# Section:      573
# Assignment:   Team Lab Topic 2 (2.8)
# Date:         30/8/2024
#

import math

#calculates the point
def calcPoint(p1, p2, t1, t2, tA):
    num = ((p2 - p1)/(t2-t1)) * (tA - t1) + p1
    return num
#calculates the distance relative to houston 
def calcDistHouston(dist):
    return dist % (rEarth * 2 * math.pi)

#variables
x1 = 2028
t1 = 10

x2 = 23028
t2 = 55

tA = 25.0

rEarth = 6745

#output
print("Part 1:\nFor t = ", int(tA), " minutes, the position p = " , calcPoint(x1, x2, t1, t2, tA), " kilometers",sep="")
tA = 300
print("Part 2:\nFor t = ", int(tA), " minutes, the position p = " , calcDistHouston(calcPoint(x1, x2, t1, t2, tA)), " kilometers",sep="")
