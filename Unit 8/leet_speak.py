# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Alexander So
# Section:      573
# Assignment:   Lab 8.18.1
# Date:         10-10-24
#

#creates dictionary
leetDict = {
    "a":"4",
    "e":"3",
    "o":"0",
    "s":"5",
    "t":"7"
}

#gets user input
textInput = input("Enter some text: ")
convertedInput = ""

#converts to leet speak
for char in textInput:
    if char.lower() in leetDict:
        convertedInput += leetDict.get(char.lower())
    else:
        convertedInput += char

print(f'In leet speak, "{textInput}" is: \n{convertedInput}')