# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Alexander So
# Section:      573
# Assignment:   4.20
# Date:         9-12-2024
#

#takes user input
days = float(input("Please enter a positive value for day: "))
print()
#checks input validity
if(days >= 0):
    total = ((((days) if days < 101 else 100)*10 + (((days-10) if days <= 50 else 40)/2) * (1 + (days - 10 if days <= 50 else 40)))) if days - 10 >= 0 else days * 10
    total += 40 * (days - 50 if days < 101 else 50) if days > 50 else 0
    print("The sum total number of gadgets produced on day", str(int(days)), "is", str(int(total)))
else:
    print("You entered an invalid number!")