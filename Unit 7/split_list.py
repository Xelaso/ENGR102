# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Alexander So
# Section:      573
# Assignment:   7.20
# Date:         9-24-24
#

#checks if the two sides are equal
def checkEqual(index, arr):
    sum1 = 0
    sum2 = 0
    for i in range(0, index):
        sum1 += arr[i]
    for i in range(index, len(arr)):
        sum2 += arr[i]
    if(sum1 == sum2):
        return sum1
    return -1

#converts a string of numbers into an integer array
def convertToList(str):
    arr = str.split()
    finalArr = []
    for i in arr:
        finalArr.append(int(i))
    return finalArr

#prints both sides
def printSides(index, arr):
    print('Left: [', end='')
    for i in range(0, index-1):
        print(arr[i], ', ', sep='', end='')
    print(arr[index-1], ']', sep='')
    print('Right: [', end='')
    for i in range(index, len(arr) - 1):
        print(arr[i], ', ', sep='', end='')
    print(arr[len(arr) - 1], ']', sep='')


#takes user input and converts it
userArr = input("Enter numbers: ")
intArr = convertToList(userArr)

#iterates through the possible splits

checkFlag = False

for i in range(0, len(intArr)):
    num = checkEqual(i, intArr)
    if(num != -1):
        checkFlag = True
        printSides(i, intArr)
        print("Both sum to", num)
if(not checkFlag):
   print("Cannot split evenly")