# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Alexander So
# Section:      573
# Assignment:   Lab 6.20
# Date:         9-24-24
#

#input
n1 = int(input("Enter a value for n: "))

#getting sum of 1-n1
n1Sum = 0 
for i in range (1, n1 + 1):
    n1Sum += i

#going until cSum passes n1
cSum = 0
itr = n1 + 1
count = 0
while(cSum < n1Sum):
    cSum += itr
    itr += 1
    count+=1

#conditional output
if(cSum == n1Sum):
    print(f'{n1} is a co-balancing number with r={count}')
else:
    print(f'{n1} is not a co-balancing number')
