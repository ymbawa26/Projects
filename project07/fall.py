# template written by Bruce A. Maxwell
# updated by Yazam Bawaqna
# Fall 2019
# CS 152
# Project 8

import graphicsPlus as gr
import physics_objects as pho
import random
import time

# main function for implementing the test code
def main():

    # create a graphics window
    win = gr.GraphWin("Falling", 500, 500, False)

    # create a ball
    # move it to the center of the screen and draw it
    # give it a random velocity
    # set the acceleration to (0, -20)

    while True:
        # call the ball's update method with a dt of 0.033
        
        time.sleep( 0.033 ) # have the animation go at the same speed

        if win.checkKey() == 'q': # did the user type a 'q'?
            break
        
        if win.checkMouse(): # did the user click the mouse?
            break

        # if the ball is outside the window
           # reposition the ball to the center of the window
           # give it a random velocity

    win.close()

if __name__ == "__main__":
    main()