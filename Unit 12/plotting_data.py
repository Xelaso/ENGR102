# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Alexander So
# Section:      573
# Assignment:   Lab Topic 12 Individual
# Date:         11-9-2024
#

import numpy as np
import matplotlib.pyplot as plt



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
    if(dayList[2] != '' and dayList[3] != '' and dayList[1] != ''):
        finalList.append(dayList)
max = -1
min = 100000000

#get max and min
for day in finalList:
    try:
        min = int(day[2]) if int(day[2]) < min else min
    except:
        continue



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




fig, ax1 = plt.subplots()

dates = np.arange(0, len(finalList))

avg_temperature = [int(day[2]) for day in finalList]


avg_wind_speed = [float(day[4]) for day in finalList]
#1
ax1.plot(dates, avg_temperature, color="red", label="Avg Temperature (°F)")
ax1.set_xlabel("Date")
ax1.set_ylabel("Avg Temperature (°F)", color="red")

ax1.tick_params(axis="y", labelcolor="red")

ax2 = ax1.twinx()
ax2.plot(dates, avg_wind_speed, color="blue", label="Avg Wind Speed (mph)")
ax2.set_ylabel("Avg Wind Speed (mph)", color="blue")

ax2.tick_params(axis="y", labelcolor="blue")


ax1.legend()
ax2.legend()

ax1.set_ylim(0, 100)
ax2.set_ylim(0, 20)
ax1.set_yticks(range(0, 101, 10))
ax2.set_yticks(np.arange(0, 20+2.5, 2.5))

fig.suptitle("Average Temperature and Wind Speed")
plt.tight_layout()
plt.show()

#2
fig, ax = plt.subplots()
ax.set_xlabel("Avg Wind Speed (mph)", color="blue")
ax.set_ylabel("Number of Days", color="blue")
fig.suptitle("Histogram of Average Wind Speed")
ax.hist(avg_wind_speed, bins=25, color='green', edgecolor='black')
plt.show()


#3
fig, ax = plt.subplots()
y = [int(day[3]) for day in finalList]
fig.suptitle("Avg relative humidity vs Avg dew point")

x =[int(day[1]) for day in finalList]
ax.set_xlabel("Avg dew point (F)", color="black")
ax.set_ylabel("Avg relative humidity (%)", color="black")
plt.scatter(x, y, s=3, color = 'black')
plt.show()

#4
fig, ax = plt.subplots()

heights = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
monthCounts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
heightsMax = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
heightsMin = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000]
heightsPrecip = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
curYear = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for day in finalList:
    monthNum = int(day[0][1])
    monthNum -= 1
    counts[monthNum] += 1
    if(int(day[0][0]) > curYear[monthNum]):
        curYear[monthNum] = int(day[0][0])
        monthCounts[monthNum] += 1
    heights[monthNum] += int(day[2])
    heightsMax[monthNum] = int(day[2]) if heightsMax[monthNum] < int(day[2]) else heightsMax[monthNum]
    heightsMin[monthNum] = int(day[2]) if heightsMin[monthNum] > int(day[2]) else heightsMin[monthNum]
    heightsPrecip[monthNum] += float(day[7])

for i in range(12):
    heights[i] /= counts[i]
    heightsPrecip[i] /= monthCounts[i]


x =[i + 1 for i in range(12)]
y = heights
ax.bar(x, y)
ax.set_xlim(0, 13)
ax.set_xticks(range(0, 13, 1))
ax.set_ylim(0, 100)
y = heightsMax
ax.plot(x, y, color='red', label='High')
y=heightsMin
ax.plot(x, y, color='blue', label='Low')
y=heightsPrecip
ax.plot(x, y, color='green', label='Precipitation')
ax.legend()

ax.set_xlabel("Month", color="black")
ax.set_ylabel("Average Temperature (F)\nMonthly Precipitation (in)", color="black")
fig.suptitle("Temperature and Precipitation by Month")
plt.show()