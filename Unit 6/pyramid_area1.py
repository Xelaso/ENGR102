# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Alex So
#               Garret Sumpter
#               Zane Aschenback
#               Clint Smith
# Section:      573
# Assignment:   Lab 6.11
# Date:         9-26-2024
#

#calculates the surface area of a given layer
def calcLayerArea(layer, sideL):
    return ((layer - 1) * 6 + 5) * sideL ** 2

#user input
sideL = float(input("Enter the side length in meters: "))
layerAmt = int(input("Enter the number of layers: "))

totalA = 0

#loops through each layer and adds the surface area to the total
for i in range(1, layerAmt + 1):
    totalA += calcLayerArea(i, sideL)
#print total area
print(f'You need {totalA:.2f} m^2 of gold foil to cover the pyramid')