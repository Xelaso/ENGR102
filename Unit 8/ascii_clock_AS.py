# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Alex So
#               Garret Sumpter
#               Zane Aschenback
#               Clint Smith
# Section:      573
# Assignment:   Lab 8.17
# Date:         10-10-24
#

def formatTime(character, hour, minute, format):
    time = ""

    #checks the format
    if(format == 12):

        #sets the AM/PM
        dayHalf = 0 if hour < 12 else 1
        #ensures hour is <= 12
        hour = hour - 12 if hour > 12 else hour
        #checks for edgecase of midnight
        if hour == 0:
            hour = 12
        #builds the output
        for i in range(5):
            mid = " : " if (i == 1 or i == 3) else "   "
            time += ((numbers[hour // 10][i] + " " if hour // 10 > 0 else "") + numbers[hour % 10][i] + mid + numbers[minute // 10][i] + " " + numbers[minute % 10][i] + " " + ampm[dayHalf][i] + "\n")
    else:
        #builds the output
        for i in range(5):
                mid = " : " if (i == 1 or i == 3) else "   "
                time += ((numbers[hour // 10][i] + " " if hour // 10 > 0 else "") + numbers[hour % 10][i] + mid + numbers[minute // 10][i] + " " + numbers[minute % 10][i] + "\n")
    
    #replaces digits with the user given character, if needed
    if(character != ""):
        time = time.replace(str(hour // 10), character)
        time = time.replace(str(hour % 10), character)
        time = time.replace(str(minute // 10), character)
        time = time.replace(str(minute % 10), character)
    
    return time