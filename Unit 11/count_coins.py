# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Alexander So
# Section:      573
# Assignment:   Lab 11.15.1
# Date:         10-31-24
#

filename = 'game.txt'
info = ''
#opens and read from file
with open(filename, 'r') as file:
    info = file.read()
#splits info into array of actions
info = info.split('\n')
count = 0
i = 0
coinChangelog = []
#loops through actions and does the correct action
while i < len(info):
    instr = info[i]
    parts = instr.split()
    action = parts[0]
    num = int(parts[1][1:])
    sign = parts[1][0]
    change = num * (-1 if sign == '-' else 1)
    if action == 'coin':
        count += change
        coinChangelog.append(change)
    elif action == 'jump':
        i += change
        continue
    i+=1
#writes to output
with open('coins.txt', 'w') as outFile:
    for coin in coinChangelog:
        outFile.write(f'{coin}\n')
#prints count
print(f'Total coins collected: {count}')