# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Alex So
#               Garret Sumpter
#               Zane Aschenback
#               Clint Smith
# Section:      573
# Assignment:   Lab 4.17
# Date:         9-12-2024
#

#evaluates user input
def evalBool(inputStr):
    return bool(inputStr.lower() == 'true' or inputStr.lower() == 't')

############ Part A ############
a = evalBool(input("Enter True or False for a: "))
b = evalBool(input("Enter True or False for b: "))
c = evalBool(input("Enter True or False for c: "))

############ Part B ############
print("a and b and c:", a and b and c)
print("a or b or c:", a or b or c)

############ Part C ############
print("XOR:", not(a and b) and (a or b))
print("Odd number:", (a and b and c) or (not(a and b) and not(b and c) and not(c and a) and not(not(a) and not(b) and not(c))))
'''
############ Part D ############

complex1 = (not (a and not b) or (not c and b)) and (not b) or (not a and b and not c) or (a and not b)
compex2 = (not ((b or not c) and (not a or not c))) or (not (c or not (b and c))) or (a and not c) and (not a or (a and b and c) or (a and ((b and not c) or (not b))))
'''