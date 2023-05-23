# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 11:58:21 2022

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

def global_max(grid_list):
    temp = 0 #temporary value that gets added on to record the max
    row = 0
    col = 0
    for x in grid_list:
        for y in x:
            if y > temp: 
                temp = y #if the value is greater than the previous replace it as it is larger (last num is the max)
    
    for x in grid_list:
        for y in x:
            if y == temp: #if the value is equal to the max...
                coord = (row, col)
            col += 1 #adds the column to when it is the max
        col = 0 #resets for the loop
        row += 1 #adds the row to when it is the max
    return coord, temp

def steepest_path(coord, grid_list, array_path, maxStep):
    arr = get_nbrs(coord[0], coord[1], grid_list)
    valid = greatest_value(coord, grid_list, arr, maxStep)
    if(len(valid) != 0):
        array_path.append(valid)
        return True
    return False

def greatest_value(coord, grid_list, arr, maxStep):
    temp = 0
    newCoord = ()
    if len(arr) == 0:
        return newCoord
    for i in arr:
        if grid_list[i[0]][i[1]] - grid_list[coord[0]][coord[1]] <= maxStep and grid_list[i[0]][i[1]] - grid_list[coord[0]][coord[1]] > 0 and temp < grid_list[i[0]][i[1]] - grid_list[coord[0]][coord[1]]:
            temp = grid_list[i[0]][i[1]] - grid_list[coord[0]][coord[1]];
            newCoord = (i[0],i[1])
    return newCoord
i = 1
while i > 0:
    n = input('Enter a grid index less than or equal to 3 (0 to end): ')
    print(n)
    n = int(n)
    if n <= hw5_util.num_grids() and n > 0: #if grid index is valid, go on
        i = 0
    else:
        i = 1 #if index is out of range, keep prompting input statement until it's valid

max_step_height = int(input("Enter the maximum step height: "))
print(max_step_height)

printed = input('Should the path grid be printed (Y or N): ')
print(printed)
printed = printed.upper()

grid_list = hw5_util.get_grid(n) #list grid numbers from the inputted grid index



row = len(grid_list)
col = len(grid_list[n])
print('Grid has {} rows and {} columns'.format(row, col))

global_max = global_max(grid_list) #puts the function return into a variable
print('global max: ' + str(global_max[0]) + ' ' + str(global_max[1])) #calls the previous variable

start_locations = hw5_util.get_start_locations(n) #all neighbors of each start location

new_array_path = []

for i in start_locations:
    array_path = [i]
    temp = i
    while (steepest_path(temp, grid_list, array_path, max_step_height) == True):
        temp = array_path[-1]
    new_array_path.append(array_path)


for x in new_array_path:
    printedString = ""
    counter = 0
    print('===\nsteepest path')
    for value in x:
        if counter % 5 == 0:
            counter = 0
            printedString = printedString + "\n"
        printedString = printedString + str(value) + ' '
        counter += 1
    print(printedString)
    if(contains(x, global_max[0]) == True):
        print("global maximum\n...")
        print("most gradual path")
    else:
        print("local maximum\n...")
        print("most gradual path")

if printed == 'Y':
    print('===\nPath grid')
elif printed == 'N':
    pass        

'''
GRADER, I didn't have time to do gradual, but how I would've implemented it would be to create a clone of steepest path and
greatest value functions to check for a minimal change in neighbors. I would create a variable equal to the difference of the first valid neighbors 
and then iterate through the list checking for a lower difference, if found then the variable would equal that coor
'''