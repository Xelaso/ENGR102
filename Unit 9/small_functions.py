# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Alexander So
# Section:      573
# Assignment:   Lab 9.20
# Date:         10-21-24
#

import math

#part a
def parta(sRad, hRad):
    return (4/3) * math.pi * (sRad**2 - hRad**2)**(3/2)


#part b
def partb(n):
    #loops through all the possible starting even values
    for start in range(2, n, 2):  
        sum = 0
        nums = []
        #sums all values from start to n
        for eNum in range(start, n + 1, 2):
            sum += eNum
            nums.append(eNum)
            #if equal to n, return
            if sum == n:
                return nums
            #if greater than n, break and go to next start
            if sum > n:
                break
    
    return False


#part c
def partc(c, name, uni, email):
    #gets the length of longest string
    longest = max(len(name), len(uni), len(email))
    longest += 4
    #constructs card
    card = c * (2+longest) + "\n" + c + name.center(longest) + c+ "\n"+c + uni.center(longest) + c+"\n"+c + email.center(longest) + c+"\n" + c* (2+longest)
    return card

#part d
def partd(arr):
    arr.sort()
    #gets minimum value
    minVal = min(arr)
    #gets maximum value
    maxVal = max(arr)
    #gets median value
    if len(arr) % 2 == 0:
        median = (arr[math.ceil((len(arr)-1) / 2)] + arr[math.floor((len(arr)-1) / 2)]) / 2
    else:
        median = arr[len(arr) // 2]
    return (minVal, median, maxVal)

#part e
def parte(times, distances):
    v = []
    
    # loop through each value starting at 2nd value
    for i in range(1, len(times)):
        # calc the change in distance and time
        deltaD = distances[i] - distances[i - 1]
        deltaT = times[i] - times[i - 1]
        
        # calc velocity as change in distance over change in time
        velocity = deltaD / deltaT
        v.append(velocity)
    
    return v

#part f
def partf(nums):
    #keeps track of seen numbers
    seen = []
    for i in nums:
        #checks if the compliment exists
        comp = 2028 - i
        if comp in seen:
            return comp * i
        seen += [i]
    return False

#part g
def partg(x, tolerance):
    sum = 0
    n = 1
    #until the term is less than tolerance, loop and add term to sum
    while True:
        term = (2/(2*n - 1)) * x **(2*n - 1)
        sum += term
        if abs(term) < tolerance:
            break
        n+=1
    return sum
        
print(partg(.5, 1e-6))