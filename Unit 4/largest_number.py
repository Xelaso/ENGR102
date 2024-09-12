# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Alexander So
# Section:      573
# Assignment:   Lab 4.18
# Date:         9-12-2024
#

#taking user input
a = float(input("Enter number 1: "))
b = float(input("Enter number 2: "))
c = float(input("Enter number 3: "))
if (c > a):
    if(c > b):
        print("The largest number is", c)
    else:
        print("The largest number is", b)
else:
    if(a > b):
        print("The largest num ber is", a)
    else:
        print("The largest number is", b)