# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Alex So
#               Garret Sumpter
#               Zane Aschenback
#               Clint Smith
# Section:      573
# Assignment:   Lab 11.9
# Date:         10-29-24
#


#takes file name input
filename = input("Enter the name of the file: ")

passportList = ''

#opens file to read
with open(filename, "r") as file:
    passportList = file.read()

#splits by passport
passportList = passportList.split("\n\n")
validList = []

#validates passports
for passport in passportList:
    if('byr' in passport and 'eyr' in passport and 'hgt' in passport and 'hcl' in passport and 'ecl' in passport and 'pid' in passport and 'cid' in passport):
        validList.append(passport)

#prints valid passport count
print(f'There are {len(validList)} valid passports')

#writes valid passports to file
with open("valid_passports.txt", 'w') as outfile:
    for passport in validList:
        outfile.write(passport + "\n\n")

