# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Alex So
#               Zane Aschenback
#               Garett Sumpter
#               Clint Smith
# Section:      573
# Assignment:   Lab 3.17 Unit Conversions
# Date:         3/9/2024
#

import math

#user input
toConvert = float(input("Please enter the quantity  to be converted: "))
value = "{num:.2f}"
value = value.format(num = toConvert)
print("\n" + value + " pounds force is equivalent to " + str(f'{(toConvert * 4.4482216153 ):.2f}') + " newtons")
print(value + " meters is equivalent to " + str(f'{(toConvert * 3.280839895):.2f}') + " feet")
print( value + " atmospheres is equivalent to " + str(f'{(toConvert * 101.325):.2f}') + " kilopascals")
print(value + " watts is equivalent to " + str(f'{(toConvert * 3.412141633 ):.2f}') + " BTU per hour")
print(value + " liters per second is equivalent to " + str(f'{(toConvert * 15.850323140625):.2f}') + " US gallons per minute")
print (value + " degrees Celsius is equivalent to " + str(f'{(toConvert * 9.0/5 + 32):.2f}') + " degrees Fahrenheit")
