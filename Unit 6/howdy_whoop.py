# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Alexander So
# Section:      573
# Assignment:   Lab 6.16
# Date:         9-24-24
#

#takes input
num1 = int(input("Enter an integer: "))
num2 = int(input("Enter another integer: "))

#iterates through and prints output
for i in range(1, 101):
    if(i % num1 != 0 and i % num2 != 0):
        print(i)
        continue
    flag = False
    if(i % num1 == 0):
        print('Howdy', end='')
        flag = True
    if(i % num2 == 0):
        if(flag):
            print(" ", end='')
        print('Whoop', end = '')
    print()