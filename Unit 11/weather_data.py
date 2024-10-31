# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Alexander So
# Section:      573
# Assignment:   Lab 11.17
# Date:         10-31-24
#


def getRange(month, year, list):
    start = -1
    end = len(list)
    for i in range(len(list)):
        if start == -1 and int(list[i][0][0]) == year and int(list[i][0][1]) == month:
            start = i
        elif start != -1 and (int(list[i][0][0]) != year or int(list[i][0][1]) != month):
            end = i
            break
    return range(start, end)


#takes input
filename = 'WeatherDataCLL.csv'
#reads from file
with open(filename, 'r') as file:
    info = file.read()
info = info.split('\n')

finalList = []

#formats array
first = True
for day in info:
    if first:
        first = not first
        continue
    dayList = day.split(',')
    dateList = dayList[0].split('-')
    dayList[0] = dateList
    finalList.append(dayList)
max = -1
min = 100000000

#get max and min
for day in finalList:
    try:
        mintemp = float(day[6])
        maxtemp = float(day[5])
        max = maxtemp if maxtemp > max else max
        min = mintemp if mintemp < min else min
    except:
        continue

print(f'10-year maximum temperature: {int(max)} F\n10-year minimum temperature: {int(min)} F')
#takes user input
month = input('Please enter a month: ')
year = int(input('Please enter a year: '))
months = {
    "january": 1,
    "february": 2,
    "march": 3,
    "april": 4,
    "may": 5,
    "june": 6,
    "july": 7,
    "august": 8,
    "september": 9,
    "october": 10,
    "november": 11,
    "december": 12
}
#converts month to number
imonth = months[month.lower()]

avgTemp = 0
avgDew = 0
avgHumid = 0
avgWind = 0
nonZPrecip = 0
totalDay = 0
#calculate averages
for i in getRange(imonth, year, finalList):
    try:
        day = finalList[i]
        avgDew += float(day[1])
        avgTemp += float(day[2])
        avgHumid += float(day[3])
        avgWind += float(day[4])
        nonZPrecip += 1 if float(day[7]) != 0 else 0
        totalDay += 1
    except:
        continue
#finalizes averages
avgTemp = round(avgTemp / totalDay, 1)
avgDew = round(avgDew / totalDay, 1)
avgHumid = round(avgHumid / totalDay, 1)
avgWind = round(avgWind / totalDay, 2)
nonZPrecip = round(nonZPrecip * 100 / totalDay, 1)

avgWind = f"{avgWind:.2f}"

print(f'For {month} {year}:\nMean average daily temperature: {avgTemp} F\n\
Mean average daily dew point: {avgDew} F\nMean relative humidity: {avgHumid}%\n\
Mean daily wind speed: {avgWind} mph\nPercentage of days with precipitation: {nonZPrecip}%')
