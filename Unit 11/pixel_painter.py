# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Alexander So
# Section:      573
# Assignment:   Lab 11.16
# Date:         10-31-24
#
#takes input
filename = input('Enter the filename: ')
character = input('Enter a character: ')
info = ''
#reads from file
with open(filename, 'r') as file:
    info = file.read()
info = info.split('\n')
output = ''

#creates the output
for line in info:
    nums = line.split(',')
    flag = True
    for num in nums:
        num = int(num)
        if flag:
            output += ' '*num
        else:
            output += character * num
        flag = not flag
    output += "\n"

#creates output file name
outFile = filename.split('.')[0] + ".txt"
#writes to output file
with open(outFile, 'w') as outputFile:
    outputFile.write(output)

print(outFile + " created!")
