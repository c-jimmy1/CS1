# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 00:41:57 2022

@author: jc219
this file contains the class used for the hw parts
This file manages bear movements
"""

from BerryField import *


class Bear(object):
    def __init__(self, row, col, direction):
        self.row = row
        self.col = col
        self.direction = direction
        self.eat_count = 0 # how many berries each bear eats
        self.sleep_turns = 0 # how many turns the bear sleeps for

    
    def __str__(self):
        self.row = self.row
        self.col = self.col
        self.direction = str(self.direction)
        return 'Bear at ({},{}) moving {}'.format(str(self.row), str(self.col), self.direction) # printing the format
    
    def move(self, grid):
        
        if self.direction == "N": # if the direction is N, -1 from row
            self.row -= 1
        elif self.direction == "E": # if the direction is E, +1 from col
            self.col += 1
        elif self.direction == "S": # if the direction is S, +1 from row
            self.row += 1
        elif self.direction == "W": # if the direction is W, -1 from col
            self.col -= 1
        elif self.direction == "NE": # if the direction is NE, -1 from row and +1 from col
            self.row -= 1
            self.col += 1
        elif self.direction == "SE": # if the direction is SE, +1 from row, and +1 from col
            self.row += 1
            self.col += 1
        elif self.direction == "SW": # if the direction is SW, +1 from row, and -1 from col
            self.row += 1
            self.col -= 1
        elif self.direction == "NW": #if the direction is NW, -1 from row, and -1 from col
            self.row -= 1
            self.col -= 1
    
        if self.row >= 0 and self.col >= 0 and self.row < len(grid.grid) and self.col < len(grid.grid): # checks for out of bounds
               return True # if not outof bounds return True
        return False
        
    def eat(self, Bfield):
        self.eat_count = 0 # resetting eat count
        if self.sleep_turns == 0: # if the sleep turns is 0 do below
            
            while self.eat_count != 30: # while the bear hasn't ate 30 berries
                
                found = False
                for tourist in Bfield.tourists: # for every tourist in the list of objects of tourists
                    if self.row == tourist.row and self.col == tourist.col: # if the bear is at the tourist location
                        found = True # set found to true
                        Bfield.toLeaveT.append(tourist) # add the tourist that dies to the list in Berryfield
                        Bfield.removeTourist(tourist) # remove the tourist from the list
                        self.sleep_turns += 2 # add sleep turns 
                        break
                    
                Bfield.toLeaveT = [] # resets the list
                
                if(found == True):
                    break # if found is true break the loop and move to the next bear
                
                '''The below calculates the amount of berries remaining in the spot if the bear eats in numbers less than 10'''
                berries_left = 30 - (Bfield.grid[self.row][self.col] + self.eat_count) 
                if berries_left < 0:
                    self.eat_count = 30
                    Bfield.grid[self.row][self.col] = abs(berries_left)
                else:
                    self.eat_count += Bfield.grid[self.row][self.col]
                    Bfield.grid[self.row][self.col] = 0


                if self.eat_count >= 30: # if the bear eats more than 30 berries, break the loop
                    break
                tempBool = self.move(Bfield)
                
                if tempBool == False: #if the bear goes out of bounds
                    toDelete = Bfield.bears.index(self) # find the index
                    return toDelete # return the index
                
        elif self.sleep_turns > 0: # if the sleep turns is anything above 1, dont do anything to the location of the bear
            self.sleep_turns -= 1 
        #print(toDelete)
        return -1
    
