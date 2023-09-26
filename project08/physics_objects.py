"""
Yazan Bawaqna
CS 152
Lab 07
to call this program type in the terminal: python3 physics_objects.py
This file creats a parent class, and child classes, which will be used to perform the videop visualization in collision.py
"""

from ipaddress import get_mixed_type_key
from string import whitespace
import time
import graphicsPlus as gr 

class Thing(object):
    """Parent Class for Simulated Objects"""
    def __init__(self, win, the_type):
        self.type = the_type
        self.mass = 1
        self.position = [0,0]
        self.velocity = [0,0]
        self.acceleration = [0,0]
        self.elasticity = 0
        self.scale = 10
        self.win = win
        self.vis = []
        self.color = [0,0,0]
        self.drawn = False

    def setelasitcity(self,ex,ey):
        self.elasticity = [ex,ey]

    def getelasticity(self):
        return self.elasticity[:]
    
    def getcolor(self):
        return self.color[:]

    def getscale(self):
        """This method retuns the scale factor"""
        return self.scale[:]

    def gettype(self):
        """This method returns the type of the object."""   
        return self.type[:]

    def getPosition(self):
        #return the position as a 2-element tuple
        return self.position[:]

    def getVelocity(self):
        """returns a 2-element tuple with the x and y velocities."""
        return self.velocity[:]

    def setVelocity(self, vx, vy):
        '''This method makes vx and vy the new x and y velocities of the Ball object.'''
        self.velocity = [vx, vy]
    
    def getAcceleration(self):
        '''This method returns a 2-element tuple with the x and y acceleration values.'''
        return self.acceleration[:]

    def setAcceleration(self,ax,ay):
        '''This method makes vx and vy the new x and y velocities of the Ball object.'''
        self.acceleration = [ax,ay]
    
    def getMass(self):
        """eturns the mass of the object as a scalar value"""
        return self.mass[:]
    
    def setMass(self,m):
        """ m is the new mass of the object"""
        self.mass = m

    def draw(self):
        """The method should loop over the self.vis list and have each item call its draw method, passing in the window (self.win) field. """
        for item in self.vis:
            item.draw(self.win)
            self.drawn = True

    def undraw(self):
        for item in self.vis:
            item.undraw()
        self.drawn = False

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

    def setColor(self, c): 
        """takes in an (r, g, b) tuple"""
        # if c is not None,
        if c != None:   
        #it should loop over the self.vis list and set the fill color of each object to the specified color. 
            for item in self.vis:
                item.setFill(gr.color_rgb(c[0],c[1],c[2]))

    def update(self,dt):
        """Thi function when called updates the velocity and the posiiton of the object"""
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




class Ball(Thing):
    def __init__(self,win):
        Thing.__init__(self,win,"ball")
        self.Radius = 1
        self.refresh() 
        self.setColor

    def refresh(self):
        drawn = self.drawn
        if drawn == True:
            self.undraw()
        self.vis = [gr.Circle( gr.Point(self.position[0]*self.scale, self.win.getHeight()-self.position[1]*self.scale), self.radius * self.scale ) ]
        if drawn == False:
            self.draw()


    def getRadius(self):
        # Returns the radius of the Ball as a scalar value
        return self.Radius
        

    def setRadius(self,r):
        #r is the new radius of the Ball object. 
        r == self.Radius
        self.refresh()


class block(Thing):
    def __init__(self, win,x0=0,y0=0,width=2,height=1, color=None):
        Thing.__init__(self, win, "block")
        self.dx = width
        self.dy = height
        self.position = [x0, y0]
        self.reshape()
        self.setColor(color)


    def reshape(self):
        """ This function redraws the objects defined in self.vis"""
        drawn = self.drawn
        #The reshape method should undraw the graphics objects if they are drawn
        if drawn:
            self.undraw()
        win = self.win
        #define the self.vis list of graphics objects using the current fields.
        self.vis = [gr.Rectangle(gr.Point((self.position[0] - (self.dx / 2)) * self.scale, win.getHeight() - ((self.position[1] - (self.dy / 2)) * self.scale)), gr.Point((self.position[0] + (self.dx / 2)) * self.scale, win.getHeight() - ((self.position[1] + (self.dy / 2)) * self.scale)))]
        #it should draw the graphics objects if they are drawn.
        if drawn:
            self.draw()

    def getWidth(self):
        """return the width or of the block."""
        return float(self.dx)
    
    def setWidth(self, w):
        """update the value of the width (dx) field"""
        self.dx = w
        #call the reshape method.
        self.reshape()

    def getHeight(self):
        """return the height of the block."""
        return float(self.dy)
    
    def setHeight(self, h):
        """update the value of the width (dx) field."""
        self.dy = h
        #call the reshape method
        self.reshape()


class Triangle(Thing):
    def __init__(self, win, width = 2, height = 2, x0 = 0, y0 = 0, color = None):
        Thing.__init__(self, win, "triangle")
        self.width = width
        self.height = height
        self.position = [x0, y0]
        self.reshape()
        self.setColor(color)
    
    def reshape(self):
        drawn = self.drawn
        if drawn:
            self.undraw()
        win = self.win
        self.vis = [gr.Polygon(gr.Point((self.position[0] - (self.width / 2)) * self.scale, win.getHeight() - ((self.position[1] - (self.height / 2)) * self.scale)), gr.Point(self.position[0] * self.scale, win.getHeight() - ((self.position[1] + (self.height / 2)) * self.scale)), gr.Point((self.position[0] + (self.width / 2)) * self.scale, win.getHeight() - ((self.position[1] - (self.height / 2)) * self.scale)))]
        if drawn:
            self.draw()

    def getWidth(self):
        """return the width or of the block."""
        return float(self.width)
    
    def setWidth(self, w):
        """update the value of the width (dx) field"""
        self.width = w
        self.reshape()
    
    def getHeight(self):
        """ return the height of the block."""
        return float(self.height)

    def setHeight(self, h= 5):
        """update the value of the width (dx) field."""
        self.height = h
        self.reshape()


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
        """update the Block position. The function must also update the graphics object&#39;s position. """
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
               
class star(Ball):
    '''This is a sublass of Ball, which is a subclass of Thing, which is a parent class of simulated objects.'''

    def __init__(self, win, radius = 1.5, x0 = 0, y0 = 0, color = None):
        '''This initializer method takes a graphics window given as the win parameter. It also has optional arguments such as radius, x0, y0, and color. The method also overrides the default set radius parameter from Ball. The object is a specialized circle where the big circle's radius is 2/3 of the given radius while the smaller circles' radius is 1/3 of the gien radius. The method lastly reshapes
        the visualization field of the object and sets the color of the visualization.'''
        Ball.__init__(self, win)
        self.radius = radius
        self.position = [x0, y0]
        self.reshape()
        self.setColor(color)

    def reshape(self):
        '''This method reshapes, or redraws, the visualization. It first checks to see if is the visualization is drawn. If it is, it undraws it and redefines the visualization field using the radius and window of the object and redraws the visualizaiton field. If it is not drawn, it still
        redefines the visualization field but not drawn onto the window.'''
        drawn = self.drawn
        #undraw if already drawn
        if drawn:
            self.undraw()
            #open a window
        win = self.win
        self.vis = [gr.Circle(gr.Point(self.position[0] * self.scale, win.getHeight() - (self.position[1] * self.scale)), self.radius * 2 / 3 * self.scale), 
        gr.Circle(gr.Point(self.position[0] * self.scale, win.getHeight() - ((self.position[1] + (self.radius * 2 / 3)) * self.scale)), self.radius * 1 / 3 * self.scale), 
        gr.Circle(gr.Point((self.position[0] + (self.radius * 2 / 3)) * self.scale, win.getHeight() - (self.position[1] * self.scale)), self.radius * 1 / 3 * self.scale), 
        gr.Circle(gr.Point(self.position[0] * self.scale, win.getHeight() - ((self.position[1] - (self.radius * 2 / 3)) * self.scale)), self.radius * 1 / 3 * self.scale), 
        gr.Circle(gr.Point((self.position[0] - (self.radius * 2 / 3)) * self.scale, win.getHeight() - (self.position[1] * self.scale)), self.radius * 1 / 3 * self.scale)]
        if drawn:
            self.draw()
        
    def setRadius(self, r):
        '''This method makes r the new radius of the object.'''
        self.radius = r
        #calling the reshaping function
        self.reshape()




