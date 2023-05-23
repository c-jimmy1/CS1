# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 01:32:43 2022

@author: jc219
this file contains the class for the hw 8
This file manages tourist leaving
"""

class Tourist(object):
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.turns = 0
        self.bears = 0
        self.death = False
    
    def __str__(self):
        self.row = self.row
        self.col = self.col
        return "Tourist at ({},{}), {} turns without seeing a bear.".format(str(self.row) , str(self.col), 0)
    
    def tooManyBears(self, bears): #calcuates the amount of bears near a tourist
        bearArea = 0  
        
        for x in bears:
            # bear near the tourists is distance formula
            if ((self.row - x.row)**2 + (self.col - x.col)**2)**(1/2) <= 4 and ((self.row - x.row)**2 + (self.col - x.col)**2)**(1/2) != 0:
                bearArea += 1
        
        return bearArea >= 3
    