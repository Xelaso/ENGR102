# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Alex So
#               Garret Sumpter
#               Zane Aschenback
#               Clint Smith
# Section:      573
# Assignment:   Lab 6.12
# Date:         9-26-2024
#



#user input
sideL = float(input("Enter the side length in meters: "))
layerAmt = int(input("Enter the number of layers: "))

#sum from 0 to layerAmt
nSum = layerAmt * (layerAmt + 1) // 2 - layerAmt

#calculates the number of full squares in the pyramid
totalA = (nSum * 6 + 5 * layerAmt) 

#multiplies by sideL squared to get total surface area
totalA *= sideL**2

#print total area
print(f'You need {totalA:.2f} m^2 of gold foil to cover the pyramid')