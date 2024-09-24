# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Alexander So
# Section:      573
# Assignment:   Lab 6.17
# Date:         9-24-24
#

#input
n1 = int(input('Enter an integer: '))
n2 = int(input('Enter another integer: '))
#calculation
nSum = 0
for i in range(n1, n2+1):
    nSum += i

#output
print(f'The sum of all integers from {n1} to {n2} is {nSum}')