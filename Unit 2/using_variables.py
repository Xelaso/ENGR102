# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Alexander So
# Section:      573
# Assignment:   2.9 Lab Using Variables
# Date:         DAY MONTH YEAR
#

import math
#calculatings
u = 9
v = 0.0015
l = 0.875
reynoldsNum = u*l/v
print("Reynolds number is", reynoldsNum)
d = 0.028
theta = 35
braggsLaw = 2*d*math.sin(math.radians(theta))
print("Wavelength is", braggsLaw, "nm")
q = 100
d = 2
b = 0.8
productionRate = q/(math.pow((1+b*d*10), (1/0.8)))
print("Production rate is", productionRate, "barrels/day")

v = 2028
mInitial = 11000
mFinal = 8300
deltaV = v*math.log(mInitial/mFinal, math.e)
print("Change of velocity is", deltaV, "m/s")
