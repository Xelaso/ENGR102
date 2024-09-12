# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Alexander So
# Section:      573
# Assignment:   Lab 3.20 Calling Functions
# Date:         6/9/2024
#

from math import *

#function definition
def printresult(shape, side, area):
    '''Print the result of the calculation'''
    print(f'A {shape} with side {side:.2f} has area {area:.3f}')

sideL = float(input("Please enter the side length: "))
triangleA = sideL * sideL * sqrt(3) / 4
squareA = sideL * sideL
pentaA = .25 * sqrt(5 * (5 + 2 * sqrt(5))) * sideL * sideL
hexA = sideL * sideL * 3 * sqrt(3) / 2
dodecA = sideL * sideL * 3 * (2 + sqrt(3))
print()
printresult("triangle", sideL, triangleA)
printresult("square", sideL, squareA)
printresult("pentagon", sideL, pentaA)
printresult("hexagon", sideL, hexA)
printresult("dodecagon", sideL, dodecA)

