# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Alexander So
# Section:      102
# Assignment:   Lab 1 follow directions
# Date:         22/8/2024
#

import math

#returns the decreasing number
def mathFunction(place):
    num = 1.0/(10 ** place)
    return num


print("This shows the evaluation of tan(x)/x evaluated close to x=0")
print("My guess is 2")
for i in range(8):
    num = mathFunction(i)
    
    print(math.tan(num)/num)

print("\nMy guess was a bit off")