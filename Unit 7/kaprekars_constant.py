# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Alexander So
# Section:      573
# Assignment:   Lab 7.21
# Date:         9-24-24
#

#converts a given num to a list
def convertToList(num):
    num = int(num)
    arr = []
    arr.append((num // 1000) % 10)
    arr.append((num // 100) % 10)
    arr.append((num // 10) % 10)
    arr.append(num % 10)
    return arr

#gets the difference between the ascending and descending version of the given number
def getDiff(numArr):
    asc = sorted(numArr)
    des = sorted(numArr, reverse=True)
    num1 = int("".join(map(str, asc)))
    num2 = int("".join(map(str, des)))
    return num2 - num1

#gets input
num = input("Enter a four-digit integer: ")

numArr = convertToList(num)

#output
count = 1
newNum = getDiff(numArr)
print(num + " > ", end='')
if(newNum == 0):
    print(0)
    print(num, "reaches 0 via Kaprekar's routine in", 1, "iterations")
else:

    


    while(newNum != 6174):
        count+=1
        print(newNum, '> ', end='')
        numArr = convertToList(newNum)
        newNum = getDiff(numArr)

    print("6174")
    print(num, "reaches 6174 via Kaprekar's routine in", count, "iterations")


        
        