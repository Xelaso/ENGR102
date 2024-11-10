import numpy as np
import matplotlib.pyplot as plt
from math import sqrt

data = []
with open('module12quizF24.txt', 'r') as file:
    reader = file.read()
    reader = reader.split('\n')

    data = np.loadtxt(reader)  

# Makes it into a 10x10s
    array = data.reshape(10, 10)

count = [0, 0, 0, 0, 0, 0, 0, 0, 0]


for num in data:
    num = int(num)
    count[num-1] +=1

maxInd = -1
max = 0
i = 0
while i < len(count):
    if count[i] > max:
        max = count[i]
        maxInd = i    
    i += 1

#print(array)


#print(f'{max}, {maxInd}')  

sum7thRow = 0
for num in array[6]:
    num = int(num)
    sum7thRow += num

sum5thCol = 0
i = 0
while i < 10:
    num = int(array[i][4])
    sum5thCol += num
    i+= 1

#print(f'5: {sum5thCol}, 7: {sum7thRow}')

print(f'\n\n\nKey: {sum7thRow - sum5thCol + maxInd + 1}')

encryptedMessage = "IOUBWRMCLNLIOMAVPETGINERMHRNSFOSPAG"
printedAmt = 0
length = len(encryptedMessage)
key = 7
index = 0
message = ""

npArr = np.array(list(encryptedMessage))
decryptArr = npArr.reshape(length// key, key)

for col in range(decryptArr.shape[1]):
    for row in range(decryptArr.shape[0]):
        print(decryptArr[row, col], end="")
    








    

