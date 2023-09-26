"""
Yazan Bawaqna
CS 152
Lab 07
This program explores several computer graphics basics using Zelle 
"""
from ipaddress import get_mixed_type_key
from string import whitespace
import time
import graphicsPlus as gr
import random


def test1():

    #Create a GraphWin object to make a window.
    win = gr.GraphWin( "My First Window WhooHoo", 500, 500, False )

    point = gr.Point(100,200)

    #Create a Circle object and assign it to a local variable like circle.
    circle = gr.Circle(point,10)
    #Draw the Circle into the window.
    circle.draw(win)
    #we need to call the update method of the window in order to see the results.
    win.update()
    #After drawing the Circle, use the window variable to execute the method getMouse() to retrieve the location of the mouse click.
    z = win.getMouse() 
    #Print out the X and Y coordinates of the mouse click location.
    print(str(z.getX())+','+str(z.getY()))
    #Close the window.
    win.close()

def test2():
    #creating a window again
    win = gr.GraphWin( "My Second Window WhooHoo", 500, 500, False )
    #Create an empty list and assign it to a variable (e.g., shapes)
    shapes = []
    #In the while loop assign to a variable pos the return value from a call to checkMouse()
    while True:
        pos = win.checkMouse()
        #If the return from checkMouse() is not equal to None do the following:
        if pos != None:
            
            point = pos
            #Create a Circle at the location of the mouse click with a radius of 10
            circle = gr.Circle(point,10)
            #Draw the circle on the window
            circle.draw(win)
            #Set the fill color of the circle to “blue”
            circle.setFill("lightblue")
            # Add the circle to the shapes list
            shapes.append(circle)
        #use the checkKey() method to capture any character that the user typed
        win.checkKey()
        input = win.checkKey()
        #h. If the user typed a ‘q’, then break out of the loop
        if input == "q":
            break
        #call update() on the window
        win.update()
        #put the program to sleep for 0.033 seconds
        #time.sleep(0.033)
        ##randomly move all the circles in the shapes list to a new location
        #location = random.randrange(0,shapes)
    #When the loop terminates, close the window
    win.close() 
        

            
if __name__ == "__main__":
    test2()

