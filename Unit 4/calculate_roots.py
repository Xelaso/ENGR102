# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Alexander So
# Section:      573
# Assignment:   Lab 4.21
# Date:         9-21-2024
#
from math import *
a = float(input("Please enter the coefficient A: "))
b = float(input("Please enter the coefficient B: "))
c = float(input("Please enter the coefficient C: "))
print()
if(a == b == 0):
    if(c != 0):
        print("You entered an invalid combination of coefficients!")
#linear
elif(a == 0):
    x = -1 * c / b
    print("The root is x =", x)

#quadratic
else:
    if(b**2 - 4 * a * c >= 0):
        x1 = ((-1 * b + sqrt(b**2 - 4 * a * c)))/(2 * a)
        x2 = ((-1 * b - sqrt(b**2 - 4 * a * c)))/(2 * a)
        if (x1 == x2):
            print("The root is x =", x1)
        else:
            print("The roots are x =", x1, "and x =", x2)

    else:
        x = ((-1 * b))/(2 * a)
        imgNum = str(sqrt(abs(b**2 - 4 * a * c))/(2 * a)) + "i"
        print("The roots are x =", str(x) + " + " + imgNum, "and x =", str(x) + " - " + imgNum)
        