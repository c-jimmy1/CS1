# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 15:07:05 2022

@author: jc219
"""


import Ball
import random
from tkinter import *

class BallDraw(object):
    def __init__ (self, parent):
        c = 0
        colorList = ["blue", "red", "green", "yellow", "magenta", "orange"]
        self.balls_list = []
        
        while c <= 9:
            self.balls_list.append(Ball.Ball(random.randint(10, 390), random.randint(10, 390), random.randint(-8, 8), random.randint(-8, 8), random.randint(5, 10), random.choice(colorList)))
            c += 1
        
        #========DATA NEEDED FOR ANIMATION=========
        #  Here is the time in milliseconds between consecutive instances
        #  of drawing the ball.  If this time is too small the ball will
        #  zip across the canvas in a blur.
        self.wait_time = 100 

        #this will allow us to stop moving the ball when the program quits
        self.isstopped = False 

        self.maxx = 400 # canvas width, in pixels
        self.maxy = 400 # canvas height, in pixels

        #=============CREATE THE NEEDED GUI ELEMENTS===========
        ##  Create a frame, attach a canvas and 4 buttons to this frame
        ##  Buttons are used to cleanly exit the program;
        ##  to speed up or slow down the animation, and to restart 
        ##  the animation.
        ##  Canvas, like an image, is an object that we can draw objects on.
        ##  This canvas is called chart_1.  
        ##  Parent = root window, contains a frame
        ##  The frame contains the canvas and the 4 buttons.
        ##  We only care about the canvas in our animation
        self.parent = parent
        self.frame = Frame(parent)
        self.frame.pack()
        self.top_frame = Frame(self.frame)
        self.top_frame.pack(side=TOP)
        self.canvas = Canvas(self.top_frame, background="white", \
                             width=self.maxx, height=self.maxy )
        self.canvas.pack()
        self.bottom_frame = Frame(self.frame)
        self.bottom_frame.pack(side=BOTTOM)
        self.restart = Button(self.bottom_frame, text="Restart", command=self.restart)
        self.restart.pack(side=LEFT)
        self.slow = Button(self.bottom_frame, text="Slower", command=self.slower)
        self.slow.pack(side=LEFT)
        self.fast = Button(self.bottom_frame, text="Faster", command=self.faster)
        self.fast.pack(side=LEFT)
        self.quit = Button(self.bottom_frame, text="Quit", command=self.quit)
        self.quit.pack(side=RIGHT)

    def faster(self):
        if self.wait_time > 2:
            self.wait_time //= 2

    def slower(self):
        self.wait_time *= 2
            
    def restart(self):
        self.isstopped = False
        self.ball.x,self.ball.y = 80,200
        self.animate()
        
    def quit(self):
        self.isstopped = True
        self.parent.destroy()
        
    def draw_ball(self):
        #  Remove all the previously-drawn balls
        
        # Draw an oval on the canvas within the bounding box
        bounding_box = (self.ball.x-self.ball.r, \
                        self.ball.y-self.ball.r,\
                        self.ball.x+self.ball.r, \
                        self.ball.y+self.ball.r) 
        self.canvas.create_oval(bounding_box, fill=self.ball.color)
        self.canvas.update()      # Actually refresh the drawing on the canvas.

        # Pause execution.  This allows the eye to catch up
        self.canvas.after(self.wait_time)

    def animate(self):
        ##  Loop until the ball runs off the screen.
        while True:
            for ballz in self.balls_list:
                self.ball = ballz
                self.ball.check_and_reverse(self.maxx, self.maxy)
                self.draw_ball()
                self.ball.x += self.ball.dx
                self.ball.y += self.ball.dy

            self.canvas.delete("all")

        
if __name__ == "__main__":
    ##  We will create a root object, which will contain all 
    ##  our user interface elements
    ##
    root = Tk()
    root.title("Tkinter: Lab 11")

    ## Create a class to handle all our animation
    bd = BallDraw(root)

    ## Run the animation by continuously drawing the ball and then moving it
    bd.animate()

    ## This is an infinite loop that allows the window to listen to
    ## "events", which are user inputs.  The only user event here is
    ## closing the window, which ends the program. 
    root.mainloop()


    
