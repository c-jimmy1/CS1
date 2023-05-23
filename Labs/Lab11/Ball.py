# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 14:18:10 2022

@author: jc219
"""

class Ball(object):
    def __init__(self, x, y, dx, dy, r, color):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.r = r
        self.color = color
        
    def position(self):
        return (self.x, self.y)
    
    def move(self):
        self.x += self.dx
        self.y += self.dy
        
    def bounding_box(self):
        x0 = self.x - self.r
        y0 = self.y - self.r
        x1 = self.x + self.r
        y1 = self.y + self.r
        return (x0, y0, x1, y1)
    
    def get_color(self):
        return self.color
    
    def some_inside(self, maxx, maxy):
        self.maxx = maxx
        self.maxy = maxy
        while 0 < self.x + self.r and \
              self.x - self.r < self.maxx and \
              0 < self.y + self.r and \
              self.y - self.r < self.maxy:
                  return True
        return False
    
    def check_and_reverse(self, maxx, maxy):
        if self.x <= 0 or self.x >= maxx:
            self.dx = self.dx * -1
        if self.y <= 0 or self.y >= maxy:
            self.dy = self.dy * -1
        