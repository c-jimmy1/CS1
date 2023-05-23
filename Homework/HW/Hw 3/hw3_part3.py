# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 13:58:03 2022

@author: jc219
"""

import math

'''
This function calculates for the amount of tourists
if the amount of bears are 4 or less or 15 or more, the tourists are equal to 0
the second elif is for when it is under 10 bears, each bear is 10000 tourists
the last elif calculates for each bear that is over 10. those bears bring 20000 tourists each
'''
def TouristCalc(bears):
    tourists = 0
    if bears < 4 or bears > 15:
        tourists = 0
    elif bears <= 10:
        tourists = bears * 10000
    elif bears > 10:
        tourists = ((bears-10)*20000) + 100000
    return tourists

'''
This function finds the next years berries and bears using the equation given in the hw
'''
def find_next(bears, berries, tourists):
    bears_next = berries/(50*(bears+1)) + bears*0.60 - (math.log(1+tourists,10)*0.1)
    berries_next = (berries*1.5) - (bears+1)*(berries/14) - \
        (math.log(1+tourists,10)*0.05)
    if(berries_next < 0):
        berries_next = 0
    bears_next = int(bears_next)
    return (bears_next, berries_next)


bears = int(input("Number of bears => "))
print(bears)
berries = input("Size of berry area => ")
print(berries)
berries = float(berries)

'''These lists are made to be inputted all the counts over the years to find the min and max'''
bearsList = []
berriesList = []
touristsList= []

tourists = TouristCalc(bears)
print("Year\tBears\tBerry\tTourists")

#This prints the first year as it is always the same
print("1\t\t{0}\t\t{1}\t{2}".format(bears, berries, tourists))


#this adds the year stats to the list
bearsList.append(bears)
berriesList.append(berries)
touristsList.append(tourists)

year = 1
while year < 10:
    
    
    bears, berries = find_next(bears, berries, tourists) #puts the function calculation into nextnum
    tourists = TouristCalc(bears)
    
#this adds to the year stats to the list
    bearsList.append(bears)
    berriesList.append(berries)
    touristsList.append(tourists)
    
    year += 1
    print("{:n}\t\t{}\t\t{:.1f}\t{:.0f}".format(year, bears, berries, tourists))


print()

#the min and max are found using the list from earlier
maxbears = max(bearsList)
maxberries = max(berriesList)
maxtourists = max(touristsList)

minbears = min(bearsList)
minberries = min(berriesList)
mintourists = min(touristsList)

print('Min:\t{:.0f}\t\t{:0.1f}\t{:.0f}'.format(minbears, minberries, mintourists))
print('Max:\t{:.0f}\t\t{:0.1f}\t{:.0f}'.format(maxbears, maxberries, maxtourists))
