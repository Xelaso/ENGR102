# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Alexander So
# Section:      573
# Assignment:   Lab 6.18
# Date:         9-24-24
#

from math import *

#user input
n1 = int(input('Enter a positive integer: '))
print('The Juggler sequence starting at', n1, 'is:')

#calculations
count = 0
seq = [n1]
while(n1 != 1):
    if(n1 % 2 == 0):
        seq.append(floor(sqrt(n1)))
    else:
        seq.append(floor(n1 ** (3/2)))
    count += 1
    n1 = (seq[len(seq) - 1])

#output and formatting
seq = [str(x) for x in seq]
ans = ', '.join(seq)
print(ans)
print(f'It took {count} iterations to reach 1')