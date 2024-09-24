# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Alexander So
# Section:      573
# Assignment:   Lab 7.19.1
# Date:         9-24-24
#

#drops the first letter if its a consonant, otherwise it makes first letter lowercase
def dropFirstCons(name):
    vowels = ['a', 'e', 'i', 'o', 'u']
    if(name[0].lower() in vowels):
        return name.lower()
    count = 0
    for i in name:
        if(i.lower() in vowels):
            break
        count += 1
    
    return name[count:]

#takes user input
userName = input("What is your name? ")
modName = dropFirstCons(userName)
#output
print(f'{userName}, {userName}, Bo-B{modName}')
print(f'Banana-Fana Fo-F{modName}')
print(f'Me Mi Mo-M{modName}')
print(f'{userName}!')