# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Alexander So
# Section:      573
# Assignment:   Lab 7.22
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

totalCount = 0
for i in range(0, 10000):
    num = i
    numArr = convertToList(num)
    count = 1
    newNum = getDiff(numArr)
    
    if(newNum != 0):
        while(newNum != 6174):
            count+=1
            numArr = convertToList(newNum)
            newNum = getDiff(numArr)
    if(num == 0 or num == 6174):
        count = 0
    totalCount += count

print(f'Kaprekar\'s routine takes {totalCount} total iterations for all four-digit numbers')
    


        
        