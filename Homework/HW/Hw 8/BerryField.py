# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 18:45:01 2022

@author: jc219

This file contains the berryfield class for hw8
This file manages berryfield growing and bear and tourist stuff
"""


class BerryField(object):
    def __init__(self, grid, bears, tourists):
          self.grid = grid
          self.bears = bears
          self.tourists = tourists
          self.toLeaveT = []
          
    def __str__(self):
        grid = ''
        T = False
        B = False
        #print(self.grid)
        for row in range(len(self.grid)): # for every row in the array
            for col in range(len(self.grid)): # for every col in the array
                
                for bear in self.bears: # for bears in self the bear
                    if bear.row == row and bear.col == col: # if the bear is at the location index
                        B = True # set B to true
                        
                for tourist in self.tourists: # if the tourist is at the location index
                    if tourist.row == row and tourist.col == col:
                        T = True

                if B == False and T == False: # if there is no bear or tourist print the number of berries
                    grid += '{:>4}'.format(self.grid[row][col])
                if B == True and T == False: # if there is a bear and no tourist print B
                    grid += '{:>4}'.format('B')
                if T == True and B == False: # if there is a Tourist and no bear print T
                    grid += '{:>4}'.format('T')
                if B == True and T == True: # if there is both, print X
                    grid += '{:>4}'.format('X')
                    
                # reset to False for next loop
                T = False 
                B = False
                
            grid += '\n'
        return grid
    
    def getGrid(self):
        return self.grid # gets the grid of the berryfield
    
    def getBears(self):
        return self.bears # gets the bears 
        
    def removeTourist(self, tourist): # removes a tourist at the index given in the Bear file
        l = self.tourists.index(tourist)
        self.tourists.pop(l)

    def checkTourists(self, row, col): # check if a tourist is in a location
        for x in self.tourists:
            if row == x.row and col == x.col:
                return True
        return False
        
    def turn(self): # every turn, use the tooManyBears, removeTourist, and eat methods from bear class and tourist class
        toKeep = []
        toDelete = []
        for b in self.bears: # for every bear object in self.bears
            ind = b.eat(self) # use the eat method in bear class
            if ind != -1: # if the index returns is -1
                toDelete.append(ind) # add the bear that left the field
                
        for i in range(len(self.bears)): 
            if i not in toDelete: # if the bear isn't in toDelete
                toKeep.append(self.bears[i]) # add to list that have bears still in the field
            else:
                print(self.bears[i], "- Left the Field") # print the bears not in the list, the ones that left
        self.bears = toKeep
        
        for tourist in self.tourists:
            if tourist.tooManyBears(self.bears) == True: # If there are more than 3 bears around the tourist
                self.toLeaveT.append(tourist)
                self.removeTourist(tourist) # remove the tourist from the grid
            if tourist.turns == 3: # if the tourist goes through 3 turns, it gets bored so it is removed
                self.toLeaveT.append(tourist)
                self.removeTourist(tourist)
            else:
                tourist.turns += 1
                
                
            #for printing the tourists that left
            for objects in self.toLeaveT:
                print(objects, "- Left the Field")
            self.toLeaveT = []
            
    def totalberries(self):
        total = 0
        for row in self.grid:
            total += sum(row)
        return total # gets the sum of the 2d array and returns the total berries count
    
    def grow(self): # growing berries, for each turn if the berry is less than 10 and greater than 0, add one berry
        for row in range(len(self.grid)):
            for col in range(len(self.grid)):
                if self.grid[row][col] > 0 and self.grid[row][col] < 10:
                    self.grid[row][col] += 1
    
    def spread(self): #spreading berries
        for row in range(len(self.grid)):
            for col in range(len(self.grid)):
                
                if self.grid[row][col] == 0:
                    # Check the location above
                    if row > 0 and self.grid[row - 1][col] == 10:
                        self.grid[row][col] += 1
                        
                    # Check the location to the right
                    elif col < len(self.grid[row]) - 1 and self.grid[row][col + 1] == 10:
                        self.grid[row][col] += 1
                    
                    # Check the location below
                    elif row < len(self.grid) - 1 and self.grid[row + 1][col] == 10:
                        self.grid[row][col] += 1
                   
                    # Check the location to the left
                    elif self.grid[row][col - 1] == 10 and col > 0:
                        self.grid[row][col] += 1
                        
                    # Check the diagonal locations
                    # Check the location above and to the left
                    elif self.grid[row - 1][col - 1] == 10 and row > 0 and col > 0:
                        self.grid[row][col] += 1
                  
                    # Check the location above and to the right
                    elif row > 0 and col < len(self.grid[row]) - 1 and self.grid[row - 1][col + 1] == 10:
                        self.grid[row][col] += 1
                   
                    # Check the location below and to the right
                    elif row < len(self.grid) - 1 and col < len(self.grid[row]) - 1 and self.grid[row + 1][col + 1] == 10:
                        self.grid[row][col] += 1
                   
                    # Check the location below and to the left
                    elif row < len(self.grid) - 1 and col > 0 and self.grid[row + 1][col - 1] == 10:
                        self.grid[row][col] += 1