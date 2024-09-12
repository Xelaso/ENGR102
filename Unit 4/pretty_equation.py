# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Alex So
#               Garret Sumpter
#               Zane Aschenback
#               Clint Smith
# Section:      573
# Assignment:   Lab 4.16
# Date:         9-12-2024
#
# This program that computes the quadratic equation based on coefficients.

# Inputs

a = float(input('Please enter the coefficient A: '))
b = float(input('Please enter the coefficient B: '))
c = float(input('Please enter the coefficient C: '))


# Conditions for the equation

equation = ""

# Coefficient for A

if a < 0:
    if a == -1:
        equation += '- x^2'
    else: 
        equation += f'- {(a/-1):.0f}x^2'
elif a > 0:
    if a == 1:   
        equation += 'x^2'
    else:
        equation += f'{a:.0f}x^2'

# Coefficient for B
    
if b > 0:
    if b == 1:
        if a != 0:
            equation += ' + x'
        else:
            equation += 'x'
    elif a != 0:
        equation += f' + {b:.0f}x'
    elif b == 1 :
        equation += 'x'
    else:
        equation += f'{b:.0f}x'
elif b < 0:
    if b == -1:
        equation += ' - x'
    elif a != 0:
        equation += f' - {-b:.0f}x'
    else:
        equation += f'- {-b:.0f}x'

#Coefficent for C
    
if c > 0:
    if a != 0 or b != 0:
        equation += f' + {c:.0f}'
    else:
        equation += f'{c:.0f}'
elif c < 0:
    if a != 0 or b != 0:
        equation += f' - {-c:.0f}'
    else:
        equation += f'- {-c:.0f}'
    
    
# Printing the equation

print('The quadratic equation is',equation, '= 0')