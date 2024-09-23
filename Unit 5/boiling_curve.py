# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Alexander So
# Section:      573
# Assignment:   Lab 5.5.1
# Date:         9-22-2024
#

from math import *

#calculates the m value
def calcM(x1, y1, x2, y2):
    return (log(y2 / y1) / log(x2 / x1))

#approximates the y value of the point provided
def approxData(p1):
    #testing for invalid inputs
    if(p1<1.3 or p1 > 1200):
        return -1
    #if the point is between 1.3 and 5
    if(p1 <= 5):
        return 1000 * (p1 / 1.3) ** calcM(1.3, 1000, 5, 7000)
    #if the point is between 5 and 30
    if(p1 <= 30):
        return 7000 * (p1 / 5) ** calcM(5, 7000, 30, 1.5 * 10 ** 6)
    #if the point is between 30 and 120
    if(p1 <= 120):
        return (1.5 * 10 ** 6) * (p1 / 30) ** calcM(30, 1.5 * 10 ** 6, 120, 2.5 * 10 ** 4)
    #if  the point is between 120 and 1200
    if(p1 <= 1200):
        return (2.5 * 10 ** 4) * (p1 / 120) ** calcM(120, 2.5 * 10 ** 4, 1200, 1.5 * 10 ** 6)


userPoint = float(input("Enter the excess temperature: "))
approxFlux = approxData(userPoint)
if(approxFlux == -1):
    print("Surface heat flux is not available")
else:
    print("\nThe surface heat flux is approximately", int(round(approxFlux)), "W/m^2")