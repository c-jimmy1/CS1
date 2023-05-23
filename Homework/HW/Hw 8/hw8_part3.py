# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 21:36:14 2022

@author: jc219

Summary: main code for part 3, which keeps running until there are no bears left or no berries

Message to TA: Hi, I didn't get enough time to finish the parts where I add in the reserve bears and tourists
"""

import json
from Bear import Bear
from BerryField import BerryField
from Tourist import Tourist

if __name__ == '__main__':
    inputfile = input('Enter the json file name for the simulation => ').strip()
    # inputfile = 'bears_and_berries_1.json'
    print(inputfile)
    print()
    f = open(inputfile)
    data = json.loads(f.read())
    
    active_bears = []
    for location in data["active_bears"]:
        bear = Bear(location[0], location[1], location[2])# location 0 is row, location 1 is col, location 2 is the direction
        active_bears.append(bear) # adds active_bears to a list
   
    active_tourists = []
    for coord in data["active_tourists"]:
         tour = Tourist(coord[0], coord[1])# location 0 is row, location 1 is col
         active_tourists.append(tour) # adds active_tourists to a list
         
    berryfields = BerryField(data["berry_field"], active_bears, active_tourists) #berryfield object
    print('Starting Configuration')
    print('Field has {} berries.'.format(berryfields.totalberries()))
    print(str(berryfields))
    


    print('Active Bears:')
    for location in active_bears:
        print(str(location))
        
    print('\nActive Tourists:')
    for coord in active_tourists:
        print(str(coord))
    
    i = 1
    while True: # looping until the loop is broken due to conditions where no bears are left or no berries are left
        print('\nTurn: {}'.format(i))
        
        berryfields.grow()
        berryfields.spread()  
        berryfields.turn()
        
        if i % 5 == 0:
            print('Field has {} berries.'.format(berryfields.totalberries()))
            print(str(berryfields)) # printing the field in grid format
       
        print('Active Bears:')
        for location in berryfields.bears:
            print(str(location)) # printing each object in bears
            
        print('\nActive Tourists:')
        for coord in berryfields.tourists: # printing each object in tourists
            print(str(coord))
        
        i += 1
        
        if len(berryfields.bears) == 0:
            break
        if berryfields.totalberries() == 0:
            break
