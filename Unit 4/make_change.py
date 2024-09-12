# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Garrett Sumpter
#               Zane Aschenbeck
#               Alex So
#               Clint Smith
# Section:      573
# Assignment:   Lab Topic 4.15
# Date:         11 Sep 2024

# This program that computes the change made when someone buys something.


paid = float(input('How much did you pay?' ))
cost = float(input('How much did it cost?' ))

# To calculate the change

change = paid - cost 
print('You received $',f'{change:.2f}', 'in change. That is...')

# For quarters

quarters = int(change // 0.25)

change %= 0.25

# For dimes

dimes = int(change // 0.10)

change %= 0.10

# For nickels

nickels = int(change // 0.05)

change %= 0.05

# For pennies

pennies = int(round(change / 0.01))

change %= 0.01

# Printing Results

if quarters == 1:
    print(quarters, 'quarter')
elif quarters >= 2:
    print(quarters, 'quarters')


if dimes == 1:
    print(dimes, 'dime')
elif dimes >= 2:
    print(dimes, 'dimes')

if nickels == 1:
    print(nickels, 'nickel')
elif nickels >= 2:
    print(nickels, 'nickels')
    
if pennies == 1:
    print(pennies, 'penny')
elif pennies >= 2:
    print(pennies, 'pennies')
    
    