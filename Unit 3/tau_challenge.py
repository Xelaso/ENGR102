# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Alexander So
# Section:      573
# Assignment:   Lab 3.21 Tau Challenge
# Date:         6/9/2024
#

import math

precision = float(input("Please enter the number of digits of precision for tau: "))

num = ('{:.' + '{}'.format(int(precision)) + 'f}').format(math.tau) 

print("The value of tau to " + str(int(precision)) + " digits is: " + str(num))