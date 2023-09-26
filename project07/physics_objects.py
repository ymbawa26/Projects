"""
Yazan Bawaqna
CS 152
Lab 07
"""

from ipaddress import get_mixed_type_key
from string import whitespace
import time
import graphicsPlus as gr 
import random

class Ball(object):
    def __init__(self, win):
        self.mass = 1
        self.radius = 1
        self.position = [0,0]
        self.velocity = [0,0]
        self.acceleration = [0,0]
        self.win = win
        #add a scale field to self and give it an initial value of 10.
        self.scale = 10
        #Create a field
        #vis of self and assign it a list with one element, which is a Graphics Circle object.
        #For the anchor point x and y values use the Ball position x-value multiplied by the scale field.
        self.vis = [gr.Circle( gr.Point(self.position[0]*self.scale, self.win.getHeight() -self.position[1]*self.scale), self.radius * self.scale ) ]

    def draw(self):
        """The method should loop over the self.vis list and have each item call its draw method, passing in the window (self.win) field. """
        for item in self.vis:
            item.draw(self.win)

    def getPosition(self):
        """This function returns back the current poisiton of the ball as a tuple of x and y coordinates"""
        ## returns a 2-element tuple with the x, y position.
        return self.position[:]


    def setPosition(self,px,py):
        #assign to x_old the current x position
        x_old = self.position[0]
        # assign to y_old the current y position
        y_old = self.position[1]
        # assign to the x coordinate in self.pos the new x coordinate
        self.position[0] = px
        # assign to the y coordinate in self.pos the new y coordinate
        self.position[1] = py
        # assign to dx the change in the x position times self.scale
        dx = (px - x_old)*self.scale
        # assign to dy the change in the y position times -self.scale
        dy = (py - y_old)*(-1)*(self.scale)
        # for each item in the vis field of self
        for item in self.vis:
            # call the move method of the item, passing in dx and dy
            item.move(dx,dy)

    def getVelocity(self):
        """This function returns the velocty assigned for the class ball after converting the velocity list into a tuple"""
        # returns a 2-element tuple with the x and y velocities.
        return self.velocity[:]

    def setVelocity(self,vx,vy):
        """ This function sets the argyments vx and vy as the new velocity and returns it as an ouput"""
        # vx and vy are the new x and y velocities
        return [vx,vy]
    
    def getAcceleration(self):  
        """ This function returns bak a tuple of the current acceleration as an ouput, first item is the acceleration in the x direction, while the second argument is the accelration in the y direction"""
        # returns a 2-element tuple with the x and y acceleration values.
        return self.acceleration[:]

    def setAcceleration(self,ax,ay):

        return [ax,ay]

    def getMass(self):
        ## Returns the mass of the object as a scalar value
        return self.mass
    
    def setMass(self,m):
        # m is the new mass of the object
        self.mass = m
        return m

    def getRadius(self):
        # Returns the radius of the Ball as a scalar value

        return float(self.radius)

    def setRadius(self, r): 
        # (**Optional**) r is the new radius of the Ball object. 
        self.radius = r

    def update(self,dt):

        # assign to x_old the current x position
        x_old = self.position[0]
        # assign to y_old the current y position
        y_old = self.position[1]
        # update the x position to be x_old + x_vel*dt + 0.5*x_acc * dt*dt
        self.position[0] = x_old + (self.velocity[0]*dt) + (0.5)*(self.acceleration[0]*dt*dt)
        # update the y position to be y_old + y_vel*dt + 0.5*y_acc * dt*dt
        self.position[1] = y_old + (self.velocity[1]*dt) + (0.5)*(self.acceleration[1]*dt*dt)
        # assign to dx the change in the x position times the scale factor (self.scale)
        dx = (self.position[0]-x_old)*self.scale
        # assign to dy the negative of the change in the y position times the scale factor (self.scale)
        dy = (self.position[1]-y_old)*(-1)*(self.scale)
        # for each item in self.vis
        for item in self.vis:  
            # call the move method of the graphics object with dx and dy as arguments..
            item.move(dx,dy)
        # update the x velocity by adding the acceleration times dt to its old value
        self.velocity[0] = self.velocity[0] + (self.acceleration[0]*dt)
        # update the y velocity by adding the acceleration times dt to its old value.
        self.velocity[1] = self.velocity[1] + (self.acceleration[1]*dt)

class Block(object):
    def __init__(self,win, dx = 1, dy = 1):
        self.width = dx
        self.height = dy
        self.mass = 1
        self.horizontal = 1
        self.vertical = 1
        self.position = [0,0]
        self.velocity = [0,0]
        self.acceleration = [0,0]
        self.win = win
        self.scale = 10
        self.vis = [gr.Rectangle(gr.Point(self.position[0] + 1/2 * self.width * self.scale, win.getHeight()- self.position[1] + 1/2 * self.height * self.scale), 
        gr.Point(self.position[0] - 1/2 * self.width * self.scale, win.getHeight() - self.position[1] - 1/2 * self.height * self.scale))]

    def draw(self):
        """raw the visualization objects into the window"""
        for item in self.vis:
            item.draw(self.win)
    
    def undraw(self):
        """undraw the visualization objects. """
        #for every item in the list, draw nothing.
        for item in self.vis:
            item.draw(None)

    def getPosition(self):
        """return the position as a 2-element tuple"""
        return self.position[:]

    def setPosition(self,px,py):
        """update the Block&#39;s position. The function must also update the graphics object&#39;s position. """
        return px, py

    def setVelocity(self,vx,vy):
        """ """
        return vx,vy
    
    def getAcceleration(self):
        return self.acceleration[:]

    def setAcceleration(self,ax,ay):
        return ax,ay

    def getWidth(self):
        # return the width of the rectangle
        return self.width

    def setWidth(self):
        # (**optional**) changes the Block's width. 
        # This method will need to undraw the shapes in the vis list, create a new vis list, then draw the shapes.
        for object in self.vis:
            self.undraw(object)
        new_vis = [ gr.Circle(gr.Point(self.position[0]*self.scale, self.win.getHeight()-self.position[1]*self.scale),self.radius * self.scale ) ]
        for object in new_vis:
            self.draw(object)

    def getHeight(self):
        # return the Block's height, which is the second element of the size list. 
        return self.height
    
    def setHeight(self):
        # (**optional**) changes the Block's height. 
        # This method will need to undraw the shapes in the vis list, create a new vis list, then draw the shapes.
        for object in self.vis:
            self.undraw(object)
        new_vis = [ gr.Circle(gr.Point(self.position[0]*self.scale, self.win.getHeight()-self.position[1]*self.scale),self.radius * self.scale ) ]
        for object in new_vis:
            self.draw(object)
    
    def setColor(self, c): # takes in an (r, g, b) tuple
        self.color = c
        if c != None:
            for object in self.vis:
                object.setFill(gr.color_rgb(c[0],c[1],c[2]))


    def update(self,dt):
            # assign to x_old the current x position
        x_old = self.position[0]
        # assign to dx the change in the x position times the scale factor (self.scale)
        dx = (self.setPosition()[0] - x_old) * self.scale
        # for each item in self.vis
        for block in self.vis:
            # call the move method of the graphics object with dx and dy as arguments..
            block.move(dx, 0)
        # update the x velocity by adding the acceleration times dt to its old value
        self.velocity[0] += self.acceleration[0] * dt 
    
    def collision(self, Ball):
        """a function that returns True if the ball is intersecting the block and False otherwise."""
        # setting up the new parameters using the class attributes
        pos_ball = Ball.getPosition()
        radius = Ball.getRadius()
        pos_block = self.getPosition()
        width = self.getWidth()
        height = self.getHeight()
        # calculating the difference in x
        dx = abs(pos_ball[0] - pos_block[0])
        # calculating the difference in y 
        dy = abs(pos_ball[1] - pos_block[1])
        # if the ball hits the block at the sides, and if the ball hits the block from above or below
        if dx <= radius + width/2 and dy <= radius + height/2:
            return True
        else:
            return False

    def move(self):
        # follow-up question 2
        for object in self.vis:
            object.move(5,10)
               





