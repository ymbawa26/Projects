'''Ellen Liu
CS 152B
lab 07
Apr 5 2022'''

'''This file defines a Ball class and a Block class'''

import graphicsPlus as gr

class Ball: 
    def __init__(self, win):
        # initial parameters of ball
        self.mass = 1
        self.radius = 1
        self.position = [0, 0]
        self.velocity = [0, 0]
        self.acceleration = [0, 0]
        self.win = win
        self.scale = 10
        self.vis = [ gr.Circle(gr.Point(self.position[0]*self.scale, win.getHeight()-self.position[1]*self.scale),self.radius * self.scale ) ]

    def draw(self):
        # draw each object in vis list
        for i in self.vis:
            i.draw( self.win )
            
    def getPosition(self):
        # returns a 2-element tuple with the x, y position.
        return self.position[:]

    def getVelocity(self): 
        # returns a 2-element tuple with the x and y velocities.
        return (self.velocity)

    def setVelocity(self, vx, vy): 
        # vx and vy are the new x and y velocities
        self.velocity = [vx, vy]

    def getAcceleration(self): 
        # returns a 2-element tuple with the x and y acceleration values.
        return (self.acceleration)

    def setAcceleration(self, ax, ay): 
        # ax and ay are new x and y accelerations.
        self.acceleration = [ax, ay]

    def getMass(self): 
        # Returns the mass of the object as a scalar value
        return self.mass

    def setMass(self, m): 
        # m is the new mass of the object
        self.mass = m 

    def getRadius(self): 
        # Returns the radius of the Ball as a scalar value
        return self.radius

    def setRadius(self, r): 
        # (**Optional**) r is the new radius of the Ball object. 
        self.radius = r
    
    def setColor(self, c): # takes in an (r, g, b) tuple
        self.color = c
        if c != None:
            for object in self.vis:
                object.setFill(gr.color_rgb(c[0],c[1],c[2]))

    def setPosition(self, px, py):
        # assign to x_old the current x position
        x_old = self.position[0]
        # assign to y_old the current y position
        y_old = self.position[1]
        # assign to the x coordinate in self.pos the new x coordinate
        self.position[0] = px
        # assign to the y coordinate in self.pos the new y coordinate
        self.position[1] = py
        # assign to dx the change in the x position times self.scale
        dx = (px - x_old) * self.scale 
        # assign to dy the change in the y position times -self.scale
        dy = (py - y_old) * - self.scale
        # for each item in the vis field of self
        for ball in self.vis:
            # call the move method of the item, passing in dx and dy
            ball.move(dx, dy)

    def update(self, dt):
        # assign to x_old the current x position
        x_old = self.position[0]
        # assign to y_old the current y position
        y_old = self.position[1]
        # update the x position to be x_old + x_vel*dt + 0.5*x_acc * dt*dt
        self.position[0] = x_old + self.velocity[0] * dt + 0.5 * self.acceleration[0] * dt*dt
        # update the y position to be y_old + y_vel*dt + 0.5*y_acc * dt*dt 
        self.position[1] = y_old + self.velocity[1] * dt + 0.5 * self.acceleration[1] * dt*dt
        # assign to dx the change in the x position times the scale factor (self.scale)
        dx = (self.position[0] - x_old) * self.scale
        # assign to dy the negative of the change in the y position times the scale factor (self.scale)
        dy = - (self.position[1] - y_old) * self.scale
        # for each item in self.vis
        for ball in self.vis:
            # call the move method of the graphics object with dx and dy as arguments..
            ball.move(dx,dy)
        # update the x velocity by adding the acceleration times dt to its old value
        self.velocity[0] += self.acceleration[0] * dt 
        # update the y velocity by adding the acceleration times dt to its old value
        self.velocity[1] += self.acceleration[1] * dt


class Block:
    def __init__(self, win, dx = 1, dy = 1):
        # initial parameters of block
        self.width = dx
        self.height = dy
        self.position = [0, 0]
        self.win = win
        self.scale = 10
        self.velocity = [1, 1]
        self.vis = [gr.Rectangle(gr.Point(self.position[0] + 1/2 * self.width * self.scale, win.getHeight()- self.position[1] + 1/2 * self.height * self.scale), 
        gr.Point(self.position[0] - 1/2 * self.width * self.scale, win.getHeight() - self.position[1] - 1/2 * self.height * self.scale))]

    def draw(self):
        # draw each object into the window 
        for object in self.vis:
            object.draw (self.win)
        self.drawn = True 

    def undraw(self):
        # undraw each object from the window
        for object in self.vis:
            object.undraw ()
        self.drawn = False 

    def getPosition(self):
        # returns a 2-element tuple with the x, y position.
        return self.position[:]

    def setPosition(self, px, py):
        # assign to x_old the current x position
        x_old = self.position[0]
        # assign to y_old the current y position
        y_old = self.position[1]
        # assign to the x coordinate in self.pos the new x coordinate
        self.position[0] = px
        # assign to the y coordinate in self.pos the new y coordinate
        self.position[1] = py
        # assign to dx the change in the x position times self.scale
        dx = (px - x_old) * self.scale 
        # assign to dy the change in the y position times -self.scale
        dy = (py - y_old) * - self.scale
        # move all the items by dx and dy
        for object in self.vis:
            object.move(dx, dy)

    def getVelocity(self): 
        # returns a 2-element tuple with the x and y velocities.
        return (self.velocity)

    def setVelocity(self, vx, vy): 
        # vx and vy are the new x and y velocities
        self.velocity = [vx, vy]

    def getAcceleration(self): 
        # returns a 2-element tuple with the x and y acceleration values.
        return (self.acceleration)

    def setAcceleration(self, ax, ay): 
        # ax and ay are new x and y accelerations.
        self.acceleration = [ax, ay]

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

    def update(self, dt):
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

    def collision(self, ball):
        # a function that returns True if the ball is intersecting the block and False otherwise.
        pos_ball = ball.getPosition()
        radius = ball.getRadius()
        pos_block = self.getPosition()
        width = self.getWidth()
        height = self.getHeight()
        # difference in x
        dx = abs(pos_ball[0] - pos_block[0])
        # difference in y 
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
