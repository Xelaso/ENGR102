# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Alexander So
# Section:      573
# Assignment:   THE ASSIGNMENT NUMBER (e.g. Lab 1b-2)
# Date:         DAY MONTH YEAR
#

import math
#calculations
print("This program calculates the Reynolds number given velocity, length, and viscosity")
u = float(input("Please enter the velocity (m/s): "))
l = float(input("\nPlease enter the length (m): "))
v = float(input("\nPlease enter the viscosity (m^2/s): "))
reynoldsNum = u*l/v

print("\nReynolds number is", round(reynoldsNum))

print("\nThis program calculates the wavelength given distance and angle")
d = float(input("Please enter the distance (nm): "))
theta = float(input("\nPlease enter the angle (degrees): "))
braggsLaw = 2*d*math.sin(math.radians(theta))
txt = "{bl:.4f}"
print("\nWavelength is", txt.format(bl=round(braggsLaw, 10)), "nm")


print("\nThis program calculates the production rate given time, initial rate, and decline rate")
t = float(input("Please enter the time (days): "))
q = float(input("\nPlease enter the initial rate (barrels/day): "))
d = float(input("\nPlease enter the decline rate (1/day): "))
b = 0.8
productionRate = q/(math.pow((1+b*d*t), (1/0.8)))
txt = "{pr:.2f}"
print("\nProduction rate is", txt.format(pr = productionRate), "barrels/day")


print("\nThis program calculates the change of velocity given initial mass, final mass, and exhaust velocity")
mInitial = float(input("Please enter the initial mass (kg): "))
mFinal = float(input("\nPlease enter the final mass (kg): "))
v = float(input("\nPlease enter the exhaust velocity (m/s): "))
deltaV = v*math.log(mInitial/mFinal, math.e)
print("\nChange of velocity is", round(deltaV, 1), "m/s")
