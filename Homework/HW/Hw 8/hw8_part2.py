# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 16:29:49 2022

@author: jc219
part 2 is the updated version involving the bear moving, 
the tourists being eaten, the bears leaving the grid
"""
import json
from Bear import Bear
from BerryField import BerryField
from Tourist import Tourist

if __name__ == '__main__':
    inputfile = input('Enter the json file name for the simulation => ').strip()
    inputfile = 'bears_and_berries_1.json'
    print(inputfile)
    print()
    f = open(inputfile)
    data = json.loads(f.read())
    # print(data["berry_field"])
    # print(data["active_bears"])
    # print(data["reserve_bears"])
    # print(data["active_tourists"])
    # print(data["reserve_tourists"])
    # print()
    
    
    active_bears = []
    for location in data["active_bears"]:
        bear = Bear(location[0], location[1], location[2])# location 0 is row, location 1 is col, location 2 is the direction
        active_bears.append(bear) # adds active_bears to a list
   
    active_tourists = []
    for coord in data["active_tourists"]:
         tour = Tourist(coord[0], coord[1])
         active_tourists.append(tour)
         
    '''using the method total berries to print the total berries in a field at the momement'''

    berryfields = BerryField(data["berry_field"], active_bears, active_tourists)
    print('Starting Configuration')
    print('Field has {} berries.'.format(berryfields.totalberries()))
    print(str(berryfields))
    


    print('Active Bears:')
    for location in active_bears:
        print(str(location)) #for every object, print in string format
        
    print('\nActive Tourists:')
    for coord in active_tourists: #for every object, print in string format
        print(str(coord))
    
    
    for x in range(1,6): # runs through 5 turns
             
        print('\nTurn: {}'.format(x)) # printing turns
        berryfields.grow() # utilzing grow method to grow berries
        berryfields.spread()  # spreading the berries
        
        berryfields.turn() #utilizing the turn in berryfields that eats, kills, and etc...
        
        print('Field has {} berries.'.format(berryfields.totalberries()))
        print(str(berryfields)) #prints the berryfield in grid format
       
        print('Active Bears:')
        for location in berryfields.bears:
            print(str(location))
            
        print('\nActive Tourists:')
        for coord in berryfields.tourists:
            print(str(coord))
        
