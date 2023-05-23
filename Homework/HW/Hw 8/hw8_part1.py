# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 16:29:49 2022

@author: jc219
main program for the bears and berries program. The classes hold most of the information
The main program is just printing
"""
import json
from Bear import Bear
from BerryField import BerryField
from Tourist import Tourist

inputfile = input('Enter the json file name for the simulation => ').strip()
print(inputfile)
print()

'''Given things to open the file'''
f = open(inputfile)
data = json.loads(f.read())
# print(data["berry_field"])
# print(data["active_bears"])
# print(data["reserve_bears"])
# print(data["active_tourists"])
# print(data["reserve_tourists"])
# print()


'''Berryfields is the object'''
berryfields = BerryField(data["berry_field"], data["active_bears"],data["active_tourists"])

'''using the method total berries to print the total berries in a field at the momement'''
print('Field has {} berries.'.format(berryfields.totalberries()))

print(str(berryfields)) #prints the 2d array in a grid format

active_bears = data["active_bears"]
print('Active Bears:')
for location in active_bears: # for every location in active bears
    location2 = Bear(location[0], location[1], location[2]) # location 0 is row, location 1 is col, location 2 is the direction
    print(str(location2)) # print the string format of active_bears
    
active_tourists = data["active_tourists"]
print('\nActive Tourists:')
for coord in active_tourists: # for every coordinate in active tourists
    coord2 = Tourist(coord[0], coord[1]) #coord2 is the object with coord0 as the row and coord1 as the col
    print(str(coord2)) # print the string format of active_bears

