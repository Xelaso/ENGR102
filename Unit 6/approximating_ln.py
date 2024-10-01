# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Alex So
#               Garret Sumpter
#               Zane Aschenback
#               Clint Smith
# Section:      573
# Assignment:   Lab 6.15
# Date:         10-1-24
#
import math

#returns the term based on term and value
def approxLN(term, val):
    return ((val - 1)**term)/term

#input
val = float(input('Enter a value for x: '))
#checks for invalid input
while(True):
    
    if(val <= 0 or val > 2):
        val = float(input('Out of range! Try again: '))
    else:
        break


tol = float(input('Enter the tolerance: '))


#calculates the approximate ln value
approxVal = 0.0
count = 1
while(True):
    if(abs(approxLN(count, val)) < tol):
        break
    approxVal += (-1)**(count+1) * approxLN(count, val)
    count+=1

#prints output
print(f'ln({val}) is approximately {approxVal}')
print(f'ln({val}) is exactly {math.log(val)}')
print(f'The difference is {abs(approxVal - math.log(val))}')

