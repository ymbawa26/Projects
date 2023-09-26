# Bruce A. Maxwell
# CS 151S
# Fall 2015
#
# Project 9
# Collision handler
#
# modified slightly by Eric Aaron for CS 152, Spring '19
# updated by Bruce Maxwell for CS 152, Fall 2019
#   fixed an issue in ball-block collision that would return False when the ball was inside the block
#   updated the ball-ball collisions to use the proper ray-circle intersections

#updated by Yazan Bawaqna 


import physics_objects as pho
import math
import graphicsPlus as gr
import random

def length(v):
    """utility math function for calculating Euclidean length of a 2D vector"""
    return math.sqrt(v[0]*v[0] + v[1]*v[1])

def unit(v):
    """utility math function for creating a unit 2D vector"""
    l = math.sqrt(v[0]*v[0] + v[1]*v[1])
    if l > 0.0:
        return (v[0]/l, v[1]/l)
    return v


def collisionTest_ball_wall( ball, wall ):
    """Tests if there is a collision with the wall along the path of 
    the ball. Returns the distance to the collision or 1e+6 (a big number)"""

    # get the ball's velocity and current position
    v = unit( ball.getVelocity() )
    ballP = ball.getPosition()

    # get the position of the floor
    wallP = wall.getPosition()

    # a variation on Liang-Barsky clipping
    p1 = -v[0]
    p2 = v[0]
    if ballP[0] < wallP[0]:
        # ball is to the left of the wall, so use the left boundary and ballx + radius
        q1 = (ballP[0]+ ball.getRadius()) - (wallP[0] - wall.getWidth()*0.5)
        q2 = (wallP[0] - wall.getWidth()*0.5) - (ballP[0] - ball.getRadius())
    else:
        # ball is on the right, so subtract radius and add wall width
        q1 = (ballP[0] - (ball.getRadius())) - (wallP[0] + wall.getWidth()*0.5)
        q2 = (wallP[0] + wall.getWidth()*0.5) - (ballP[0] - (ball.getRadius()))

    # running parallel to the wall, no collision for a stationary wall
    if p1 == 0.0: 
        return 1e+6

    if p1 < 0: # ball is heading in a +y direction
        if q1 > 0: # ball is headed away from the wall
            return 1e+6
        else: # ball is headed towards the wall
            return q1 / p1
    else: # ball is heading in a -y direction
        if q2 > 0: # ball is headed away from the wall
            return 1e+6
        else:
            return q2/p2
    

def collision_ball_wall(ball, wall, dt):
    """Main collision function for handling ball/wall collisions
    Updates the ball's position and returns true if there was a collision. 
    Returns False if there was no collision (ball still needs to be udpated). """

    # returns the distance between the ball and the wall
    tk = collisionTest_ball_wall( ball, wall )
    
    d = length(ball.getVelocity())
    if d == 0.0: # special case if the ball is not moving at all
        return False

    # check if the collision will happen during dt
    delta = tk / (d*dt)
    if delta <= 1.0:

        # update to the collision
        ball.update( delta*dt )

        # change the velocity
        v = ball.getVelocity()
        be = ball.getElasticity()
        fe = wall.getElasticity()
        ball.setVelocity( -v[0]*be*fe, v[1] )

        # update after the collision
        ball.update(dt - delta*dt)

        return True

    # if no collision, calling function handles the update
    return False


def collisionTest_ball_floor( ball, floor ):
    """Tests if there is a collision with the floor along the path of the
    ball. Returns the distance to the collision or 1e+6 (a big number)"""

    # get the trajectory and position of the ball
    v = unit( ball.getVelocity() )
    ballP = ball.getPosition()

    # get the y position of the floor
    floorP = floor.getPosition()

    # a variation on Liang-Barsky clipping
    p3 = -v[1]
    p4 = v[1]
    if ballP[1] > floorP[1]:
        q3 = (ballP[1]-ball.getRadius()) - (floorP[1] + floor.getHeight()*0.5)
        q4 = (floorP[1] + floor.getHeight()*0.5) - (ballP[1] - ball.getRadius())
    else:
        q3 = (ballP[1] + ball.getRadius()) - (floorP[1] - floor.getHeight()*0.5)
        q4 = (floorP[1] - floor.getHeight()*0.5) - (ballP[1] - ball.getRadius())

    if p4 == 0.0: # parallel traejectory to the wall
        return 1e+6

    if p3 < 0: # ball is heading in a +y direction
        if q3 > 0: # ball is headed away from the wall
            return 1e+6
        else: # ball is headed towards the wall
            return q3 / p3
    else: # ball is heading in a -y direction
        if q4 > 0: # ball is headed away from the wall
            return 1e+6
        else:
            return q4/p4

def collision_ball_floor(ball, floor, dt):
    """Main collision function for handling ball/floor collisions
    Updates the ball's position and returns true if there was a collision.
    Returns False if there was no collision (ball still needs to be udpated)."""
    
    # returns the distance between the ball and the floor
    tk = collisionTest_ball_floor( ball, floor )
    
    d = length(ball.getVelocity())
    if d == 0.0:
        return False

    # check if the collision will happen during dt
    delta = tk / (d*dt)
    if delta <= 1.0:

        # update to the collision
        ball.update( delta*dt )

        # update the velocity
        v = ball.getVelocity()
        be = ball.getElasticity()
        fe = floor.getElasticity()
        ball.setVelocity( v[0], -v[1] * be * fe )

        # update after the collision
        ball.update(dt - delta*dt)

        return True

    # if no collision, calling function is responsible for the update
    return False


def collisionTest_ball_ball(ball1, ball2):
    """Tests if there is a collision with another ball along the path of
    the ball.  Returns the distance to the collision or 1e+6 (a big number)"""
    
    # Concept: hold ball2 still and test if ball1 will hit it
    # Ray-circle intersection
    v1 = ball1.getVelocity()
    p1 = ball1.getPosition()
    p2 = ball2.getPosition()
    r = ball1.getRadius() + ball2.getRadius()

    dx = p1[0] - p2[0]
    dy = p1[1] - p2[1]

    # quadratic equation
    a = v1[0]*v1[0] + v1[1]*v1[1]
    b = dx*v1[0] + dy*v1[1]
    c = dx*dx + dy*dy - r*r

    delta = b*b - a*c
    
    if  delta <= 0: # no intersection, imaginary roots
        return 1e+6

    deltaroot = math.sqrt(delta)
    t1 = (-b + deltaroot) / a
    t2 = (-b - deltaroot) / a

    if t1 < 0 and t2 < 0: # intersection is behind the ball
        return 1e+6

    # one of these could be negative
    tmin = min(t1, t2)

    # ball's already intersect, so move ball1 back to the boundary
    if t1 < 0 or t2 < 0:
        newpx = p1[0] + tmin*v1[0]
        newpy = p1[1] + tmin*v1[1]
        ball1.setPosition( newpx, newpy )
        return 0.0
        
    dx = tmin*v1[0]
    dy = tmin*v1[1]
    distToImpact = math.sqrt(dx*dx + dy*dy)

    return distToImpact
    

def collision_ball_ball(ball1, ball2, dt):
    """Main collision function for handling ball/ball collisions
    Updates the ball1's position and returns true if there was a collision.
    Returns False if there was no collision (ball1 still needs to be udpated).
    ball2's velocity is changed, but it is not updated by this function"""

    # holds ball2 steady, tests ball1's trajectory
    distToImpact = collisionTest_ball_ball(ball1, ball2)

    # get the magnitude of the velocity of ball1
    v1 = ball1.getVelocity()
    v2 = ball2.getVelocity()
    vmag1 = length( ball1.getVelocity() )

    # no collision if it's too far away
    if distToImpact > vmag1 * dt:
        return False

    # check for a stationary ball
    if vmag1 < 1e-6:
        # just update and return a collision
        ball1.update( dt )
        return True

    delta = distToImpact / (vmag1*dt)

    # don't update backwards, which can happen, strangely enough
    if delta > 0.0:
        ball1.update( delta*dt )

    p1 = ball1.getPosition()
    p2 = ball2.getPosition()
    rvec = unit( (p1[0] - p2[0], p1[1] - p2[1]) ) # reflection vector

    # create the reflection matrix R(th)M(X)R(-th)

    # update ball1's velocity
    # rotate reflection vector to the Y axis
    tvx =  rvec[0] * v1[0] + rvec[1] * v1[1]
    tvy = -rvec[1] * v1[0] + rvec[0] * v1[1]

    # mirror in X
    tvx = - float(tvx)*float(ball1.getElasticity())*float(ball2.getElasticity()) # need to add the loss factor here

    # rotate back
    vfx = rvec[0] * tvx - rvec[1] * tvy
    vfy = rvec[1] * tvx + rvec[0] * tvy

    ball1.setVelocity( vfx, vfy )

    # update ball2's velocity
    tvx =  rvec[0] * v2[0] + rvec[1] * v2[1]
    tvy = -rvec[1] * v2[0] + rvec[0] * v2[1]

    # mirror in X
    tvx = - tvx*ball1.getElasticity()*ball2.getElasticity() # need to add the loss factor here

    # rotate back
    vfx = rvec[0] * tvx - rvec[1] * tvy
    vfy = rvec[1] * tvx + rvec[0] * tvy

    ball2.setVelocity( vfx, vfy )

    # finish updating ball1
    if delta > 0.0:
        ball1.update( dt - delta*dt )
    else:
        ball1.update( dt )

    return True


def collisionTest_ball_block(ball, block):
    """Test if a ball is colliding with any side of a block, and indicate
    which side. Sends out a line along the ball's velocity vector and
    compares it with all four sides of the object."""

    # get the trajectory and position of the ball
    v = unit( ball.getVelocity() )
    ballP = ball.getPosition()
    radius = ball.getRadius()

    # get the position of the block
    blockP = block.getPosition()

    # a variation on Liang-Barsky clipping
    # expands the block by the size of the ball before testing
    dx = block.getWidth()
    dy = block.getHeight()

    p = ( -v[0], v[0], -v[1], v[1] )
    q = (ballP[0] - (blockP[0] - dx*0.5 - radius),
         (blockP[0] + dx*0.5 + radius) - ballP[0],
         ballP[1] - (blockP[1] - dy*0.5 - radius),
         (blockP[1] + dy*0.5 + radius) - ballP[1] )


    # for all four cases
    tmin = -1e+6
    tmax = 1e+6
    side = -1
    sidemax = -1
    for i in range(4):
        if p[i] == 0.0: # no collision for this side of the block, motion is parallel to it
            if q[i] < 0: # outside the boundary of the box, no collision
                return 1e+6,0
            continue

        tk = q[i] / p[i]

        if p[i] < 0: # outside moving in
            if tk > tmin:
                tmin = tk
                side = i
        else:
            if tk < tmax:
                tmax = tk
                sidemax = i

        if tmax <= tmin: # no intersection with the box
            return 1e+6,0

    if tmin < 0 and tmax < 0: # both intersections behind the ball
        tmin = 1e+6
    elif tmin < 0 and tmax > 0: # ball is intersecting the block
        #print("ball is intersecting")

        # move the ball back along its velocity to the intersection point
        if v[0] == 0.0 and v[1] == 0.0:
            v = (1.0, 0.0)
            tmin = (blockP[0] - 0.5*dx - radius) - ballP[0]

        # move it to the closest side and set distance to impact to 0
        if -tmin < tmax:
            #print("setting position using tmin and velocity %.2f %d" % (tmin, side))
            ball.setPosition( ballP[0] + (tmin+1e-3)*v[0], ballP[1] + (tmin+1e-3)*v[1])
        else:
            #print("setting position using tmax and velocity %.2f %d" % (tmax, sidemax))
            ball.setPosition( ballP[0] + (tmax+1e-3)*v[0], ballP[1] + (tmax+1e-3)*v[1])
        tmin = 0

    # tmin is the closest intersection on side i
    # 0: coming up from below
    # 1: coming down from above
    # 2: coming from the left
    # 3: coming from the right
    return (tmin, side)


def collision_ball_block(ball, block, dt):
    """Main collision code for ball/block interactions.
    Updates the ball's position and returns true if there was a collision.                                     
    Returns False if there was no collision (ball still needs to be udpated)."""

    # get distance to impact
    distToImpact, side = collisionTest_ball_block( ball, block )

    # check if the impact is farther away than one step
    vmag = length( ball.getVelocity() )
    if vmag == 0.0 or distToImpact > vmag * dt:
        return False

    # update the ball prior to the collision
    delta = distToImpact / (vmag * dt)
    ball.update( delta * dt )

    # modify the velocities
    v = ball.getVelocity()
    if side == 0 or side == 1: # left or right wall, so adjust x
        ball.setVelocity( -v[0]*ball.getElasticity()*block.getElasticity(), v[1]  )
    elif side == 2 or side == 3: # top or bottom wall, so adjust y
        ball.setVelocity( v[0], -v[1]*ball.getElasticity()*block.getElasticity()  )

    # update the ball post-collision
    ball.update( (1 - delta) * dt )

    return True

def collisionTest_block_block(block1, block2):
    """Test if a block is colliding with any side of another block, and indicate
    which side. Sends out a line along the  moving block's velocity vector and
    compares it with all four sides of the object."""

    # get the trajectory and position of the ball
    v = unit( block1.getVelocity() )
    block1P = block1.getPosition()
    width1 = block1.getWidth()
    height1 =   block1.getHeight()
    

    # get the position of the block
    block2P = block2.getPosition()

    # a variation on Liang-Barsky clipping
    # expands the block by the size of the ball before testing
    dx = block1.getWidth()
    dy = block1.getHeight()

    dx2 = block2.getWidth()
    dy2 = block2.getHeight()

    p = ( -v[0], v[0], -v[1], v[1] )
    q = (block1P[0] - (block2P[0] - dx*0.5 - dx2*0.5),
         (block2P[0] + dx*0.5 + dx2*0.5) - block1[0],
         block1[1] - (block2P[1] - dy1*0.5 - dy2*0.5),
         (block2P[1] + dy*0.5 + dy2*0.5) - block1P[1] )


    # for all four cases
    tmin = -1e+6
    tmax = 1e+6
    side = -1
    sidemax = -1
    for i in range(4):
        if p[i] == 0.0: # no collision for this side of the block, motion is parallel to it
            if q[i] < 0: # outside the boundary of the box, no collision
                return 1e+6,0
            continue

        tk = q[i] / p[i]

        if p[i] < 0: # outside moving in
            if tk > tmin:
                tmin = tk
                side = i
        else:
            if tk < tmax:
                tmax = tk
                sidemax = i

        if tmax <= tmin: # no intersection with the box
            return 1e+6,0

    if tmin < 0 and tmax < 0: # both intersections behind the ball
        tmin = 1e+6
    elif tmin < 0 and tmax > 0: # ball is intersecting the block
        #print("ball is intersecting")

        # move the ball back along its velocity to the intersection point
        if v[0] == 0.0 and v[1] == 0.0:
            v = (1.0, 0.0)
            tmin = (blockP[0] - 0.5*dx - dx2*0.5) - ballP[0]

        # move it to the closest side and set distance to impact to 0
        if -tmin < tmax:
            #print("setting position using tmin and velocity %.2f %d" % (tmin, side))
            ball.setPosition( ballP[0] + (tmin+1e-3)*v[0], ballP[1] + (tmin+1e-3)*v[1])
        else:
            #print("setting position using tmax and velocity %.2f %d" % (tmax, sidemax))
            ball.setPosition( ballP[0] + (tmax+1e-3)*v[0], ballP[1] + (tmax+1e-3)*v[1])
        tmin = 0

    # tmin is the closest intersection on side i
    # 0: coming up from below
    # 1: coming down from above
    # 2: coming from the left
    # 3: coming from the right
    return (tmin, side)
    
def collision_block_block(block1, block2, dt):
    # get distance to impact
    distToImpact, side = collisionTest_block_block( block1, block2 )

    # check if the impact is farther away than one step
    vmag = length( ball1.getVelocity() )
    if vmag == 0.0 or distToImpact > vmag * dt:
        return False

    # update the ball prior to the collision
    delta = distToImpact / (vmag * dt)
    block1.update( delta * dt )

    # modify the velocities
    v = block1.getVelocity()
    if side == 0 or side == 1: # left or right wall, so adjust x
        block1.setVelocity( -v[0]*block1.getElasticity()*block2.getElasticity(), v[1]  )
    elif side == 2 or side == 3: # top or bottom wall, so adjust y
        block1.setVelocity( v[0], -v[1]*block1.getElasticity()*block2.getElasticity()  )

    # update the ball post-collision
    ball.update( (1 - delta) * dt )

    return True
def collision_balloon_block(balloon,block, dt):
    """ """
    
    bblock = Block(balloon.getWin())
    bblock.setPosition(balloon.getPosition()[0],balloon.getPosition()[1]+balloon.getSize()*balloon.getScale()++balloon.getSize()*balloon.getScale()*7)
    ball  = Ball(balloon.getWin(),balloon.getSize()*balloon.getScale(),balloon.getPosition()[0],balloon.getPosition()[1] - balloon.getSize()*balloon.getScale())
    bblock.setHeight(balloon.getSize()*balloon.getScale()*4)

    return (collision_block_block(bblock, block, dt) or collision_ball_block(ball, block, dt))
###### collision_router and helper functions go here  ################

collision_router = {}
collision_router[ ('ball', 'ball') ] = collision_ball_ball
collision_router[ ('ball', 'block') ] = collision_ball_block
collision_router[ ('ball', 'triangle') ] = collision_ball_block
collision_router[ ('triangle', 'triangle') ] = collision_block_block
collision_router[ ('triangle', 'ball') ] = collision_ball_block
collision_router[ ('triangle,','block')] = collision_block_block

def collision(ball, thing, timestep):
    collision_router[('ball',thing.getType())](ball,thing,timestep)

def buildObstacles(win):
    """ this function creates the obstacles or the objects to be shown in the scene by assigning them there characteristics"""
     # Create all of the obstacles in the scene and put the in a list
     # Each obstacle should be a Thing (e.g. Ball, Block, other)
    leftborder = pho.Block(win, 2, 30, 10, 25, color = (10, 10, 10))
    rightborder = pho.Block(win, 2, 30, 30, 25, color = (10, 10, 10))
    topborder = pho.Block(win, 22, 2, 20, 41, color = (10, 10 , 10))
    bottomleftborder = pho.Block(win, 8, 2, 13, 9, color = (10, 10, 10))
    bottomrigthborder = pho.Block(win, 8, 2, 27, 9, color = (10, 10, 10))
    obs1 = pho.Triangle(win, x0 = 13 , y0 = 30, color = (70, 170, 50))
    obs2 = pho.Ball(win, x0 = 27, y0 = 30, color = (50, 10, 130))
    obs2.setElasticity(1.15)
    obs3 = pho.Ball(win, x0 = 15, y0 = 15, color = (134, 43, 20))
    obs3.setElasticity(1.15)
    obs4 = pho.Triangle(win, x0 = 26, y0 = 15, color = (40, 80, 160))
    obs4.setElasticity(1.15)
    obs5 = pho.Block(win, 2, 2, 15, 35, color = (77, 99, 123))
    obs6 = pho.Block(win, 2, 2, 25, 35, color = (255, 0, 0))
    obs7 = pho.Block(win, 1, 2, 20, 28, color = (225, 99, 123))

    obstacles = [leftborder, rightborder, topborder, bottomleftborder, bottomrigthborder, obs1, obs2, obs3, obs4, obs5, obs6, obs7]
    # Return the list of Things
    return obstacles


def main():
    """ This function when called creats a scene of a ball and obstancles inside of  a box as a physical interactive game. You can control the ball using the arrows"""
    # create a GraphWin
    win = gr.GraphWin("Pinball Table Simulation", 500, 500)
    win.setBackground("orange")
    # call buildObstacles, storing the return list in a variable (e.g. shapes)
    shapes = buildObstacles(win)
    # loop over the shapes list and have each Thing call its draw method
    for x in shapes:
        x.draw()
    # assign to dt the value 0.02
    dt = 0.02
     # assign to frame the value 0
    frame = 0
    # create a ball, give it an initial velocity and acceleration, and draw it
    ball = pho.Ball(win)
    ball.setRadius(0.9)
    ball.setColor([255,255,255])
    ball.setVelocity(random.randint(-10, 10), 10)
    ball.setAcceleration(0, 0)
    ball.setPosition(20,8)
    ball.draw()
    star = pho.Tetrahedral_Molecule(win)
    star.setRadius(0.8)
    star.setColor([150,150,150])
    star.setVelocity(random.randint(-10, 10), 10)
    star.setAcceleration(0, 0)
    star.setPosition(17,6)
    star.draw()

    new_obs_list =[]
    
    print('Press N to create a new obstacle and use the Arrow Keys to move it around')
    print('Press Q to quit')
    # start an infinite loop
    while True:
        # if frame modulo 10 is equal to 0
        if frame % 10 == 0:
            win.update()
        keypressed = win.checkKey()
        if keypressed == "q":
            break
        if keypressed =="n":
            newobs = pho.Block(win, color = (150, 30, 200))
            newobs.setPosition(20, 8)
            newobs.draw()
            shapes.append(newobs)
            new_obs_list = [newobs] 
        if keypressed == 'Up': # if the user pressed the up arrow key, move the most recently created obstacle created up
            for obs in new_obs_list:
                obs_pos = obs.getPosition()
                x_old = obs_pos[0]
                y_old = obs_pos[1]
                x_new = x_old
                y_new = y_old + 1
                obs.setPosition(x_new, y_new)
        
        if keypressed == 'Down': # if the user pressed the down arrow key, move the most recently created obstacle created down
            for obs in new_obs_list:
                obs_pos = obs.getPosition()
                x_old = obs_pos[0]
                y_old = obs_pos[1]
                x_new = x_old
                y_new = y_old - 1
                obs.setPosition(x_new, y_new)
        
        if keypressed == 'Left': # if the user pressed the left arrow key, move the most recently created obstacle created left
            for obs in new_obs_list:
                obs_pos = obs.getPosition()
                x_old = obs_pos[0]
                y_old = obs_pos[1]
                x_new = x_old - 1
                y_new = y_old
                obs.setPosition(x_new, y_new)
        
        if keypressed == 'Right': # if the user pressed the right arrow key, move the most recently created obstacle created right
            for obs in new_obs_list:
                obs_pos = obs.getPosition()
                x_old = obs_pos[0]
                y_old = obs_pos[1]
                x_new = x_old + 1
                y_new = y_old
                obs.setPosition(x_new, y_new)
    # if the ball is out of bounds, re-launch it
        pos = tetra.getPosition()
        if pos[0] < 10 or pos[0] > 30 or pos[1] < 7:
            tetra.setPosition(20, 8)
            tetra.setVelocity(random.randint(-10, 10), 10)
            tetra.setAcceleration(0, 0)
        

        # pos1 = newball.getPosition()
        # if pos1[0] < 10 or pos1[0] > 30 or pos1[1] < 7:
        #     newball.setPosition(20, 8)
        #     newball.setVelocity(random.randint(-20, 20), 25)
        #     newball.setAcceleration(0, 0)

        # assign to collided the value False
        collided = False
        # for each item in the shapes list
        for item in shapes:
            # if the result of calling the collision function with the ball and the item is True
            if collision(tetra, item, dt):
                collided = True
            
            # if collision(newball, item, dt):
            #     collided = True
            
        # if collided is equal to False
        if collided == False:
            # call the update method of the ball with dt as the time step
            tetra.update(dt)
            # newball.update(dt)
        # increment frame
        frame += 10
    # close the window
    win.close()

if __name__ == "__main__":
    main() 
        

