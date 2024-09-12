# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Alexander So
# Section:      573
# Assignment:   Lab 1 follow directions
# Date:         22/8/2024
#

import math

#returns the decreasing number
def mathFunction(place):
    num = 1.0/(10 ** place)
    return num


print("This shows the evaluation of (1-cos(x))/x^2 evaluated close to x=0")
print("My guess is 2")
for i in range(8):
    num = mathFunction(i)
    finalNum = (1 - math.cos(num))/(num**2)
    print(finalNum)

print("\nMy guess was a bit off")