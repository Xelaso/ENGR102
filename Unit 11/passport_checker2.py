# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Alex So
#               Garret Sumpter
#               Zane Aschenback
#               Clint Smith
# Section:      573
# Assignment:   Lab 11.10
# Date:         10-29-24
#

import re

#takes file name input
filename = input("Enter the name of the file: ")

passportList = ''

#opens file to read
with open(filename, "r") as file:
    passportList = file.read()

#splits by passport
passportList = passportList.split("\n\n")
tempPassList = passportList
finalList = []
dictList = []
validList = []

#creates finalList which stores a dictionary of each passport
for passport in passportList:
    eleList = re.split(r'\s+', passport)
    dict = {}
    for ele in eleList:
        mapping = re.split(":", ele)
        dict[mapping[0]] = mapping[1]
    finalList.append(dict)

#validates passport
for i in range(len(finalList)):
    passport = finalList[i]
    if('byr' in passport and 'eyr' in passport and 'hgt' in passport and 'hcl' in passport and 'ecl' in passport and 'pid' in passport and 'cid' in passport):
        height = False
        # Height validation
        if 'cm' in passport['hgt']:
            if 150 <= int(passport['hgt'].replace('cm', '')) <= 193:
                height = True
        elif 'in' in passport['hgt']:
            if 59 <= int(passport['hgt'].replace('in', '')) <= 76:
                height = True

        if(int(passport['byr'])  in range(1920, 2009)) and (int(passport['eyr']) in range(2024, 2035)) and height and re.fullmatch("#([0-9a-f]{6})",passport['hcl']) \
        and re.fullmatch(r"\b(amb|blu|brn|gry|grn|hzl|oth)\b", passport['ecl']) and re.fullmatch(r"\b\d{9}\b", passport['pid']) and int(passport['cid']) >= 100:
                validList.append(tempPassList[i])
#prints valid passport count
print(f'There are {len(validList)} valid passports')

#writes valid passports to file
with open("valid_passports2.txt", 'w') as outfile:
    for passport in validList:
        outfile.write(passport + "\n\n")

