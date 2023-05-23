# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 10:28:44 2022

@author: jc219
"""
import hw5_util

'''
The 4 if statements check for every single condition and adds to the list neighborsList if it is true
neighborsList returns the list of tuples of neighbors
'''
def get_nbrs(row, col, grid_list):
    neighborsList = []
    if row != 0: #if the row isnt the first row
        above = (row - 1, col) #The neighbor above is row-1
        neighborsList.append(above)
    if col != 0: #if the col isnt the first column
        left = (row, col - 1) #The neighbor next to it is col-1
        neighborsList.append(left)
    if col != len(grid_list[row]) - 1: #if the row isnt the last col
        right = (row, col + 1) # The neighbor is col+1 (right)
        neighborsList.append(right)
    if row != len(grid_list) - 1: #if the row isn't the last row
        below = (row + 1, col) #The neighbor is row+1 (below)
        neighborsList.append(below) 

    return neighborsList


def check_path(path, grid_list):
    array = [] #list of coordinates where it went incorrect
    for x in range(len(path)-1):
        nbrs_path = get_nbrs(path[x][0],path[x][1], grid_list) #gets neighbors for every coordinate path
        if contains(nbrs_path, path[x+1]) == False: #if the contains function is false, it appends the coordinates when it went wrong
            array.append(path[x]) #adds value when it went incorrect
            array.append(path[x+1]) #adds target value when it went incorrect
    return array
                
def contains(array, num): #function used in check_path
    for x in array:
        if num == x:
            return True #returns true if the next path is in neighbors of the previous
    return False

i = 1
while i > 0:
    n = input('Enter a grid index less than or equal to 3 (0 to end): ')
    print(n)
    n = int(n)
    if n <= hw5_util.num_grids() and n > 0: #if grid index is valid, go on
        i = 0
    else:
        i = 1 #if index is out of range, keep prompting input statement until it's valid
        
printed = input('Should the grid be printed (Y or N): ')
print(printed)
printed = printed.upper()

grid_list = hw5_util.get_grid(n) #list grid numbers from the inputted grid index

if printed == 'Y':
    print('Grid', n)
    for x in grid_list:
        for y in x:
            print('{:4d}'.format(y), end = '') #formatting for the grid printing
        print()
elif printed == 'N':
    pass

row = len(grid_list)
col = len(grid_list[n])
print('Grid has {} rows and {} columns'.format(row, col))

all_neighbor = hw5_util.get_start_locations(n) #all neighbors of each start location

for x in all_neighbor:
    xcoord = x[0] #xcoordinate of the tuple
    ycoord = x[1] #ycoordinate of the tuple
    printpt1 = 'Neighbors of ' + str(x) + ': '
    for i in get_nbrs(xcoord, ycoord, grid_list):
        printpt1 = printpt1 + str(i) + ' ' # for printing the tuples out of the list without brackets
    printpt1 = printpt1.strip(' ') # strips the last extra space that is created by the previous line of code
    print(printpt1)

path = hw5_util.get_path(n) #list of paths for the grid
incorrect = check_path(path, grid_list) #list of when it went incorrect path

if len(incorrect) == 0: #if the incorrect list is empty, meaning it is a valid path
    print('Valid path')
    value = []
    for x in path:
        value.append(grid_list[x[0]][x[1]]) #appends the value of the grid in according to their coordinate
        temp = value[0] #temporary value to be added on to
    downward = 0 #start at 0
    upward = 0 #start at 0
    for y in value:
        if y < temp: #if the value is less than the temporary value it moves down
            downward += temp - y #subtract the temporary value by the amount it moves down
        if y > temp: #if the value is greater than the temporary value it moves upward
            upward += y - temp #subtract the value by the previous value to get the amount it moves further (if previous is 5 and y is 7, 7-5 is 2 upward)
        temp = y
    print("Downward " + str(downward))
    print("Upward " + str(upward))
    
else:
    print('Path: invalid step from ' + str(incorrect[0]) + " to " + str(incorrect[1])) #if incorrect list has something in it print the invalid step statement
    


    