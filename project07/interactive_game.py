""" Yazan bawaqna
CS 152 B
Project 8 
Apr 13, 2022 
Credits: Help from ellen lie"""

""" This is a bouncing ball game. Control the left and right movement of the block by using 'a' and 'd'. 
 move the block to catch the ball. it will count how many times the ball hits the block. 
 type 'python3 ball_game.py to play.  """

import graphicsPlus as gr
import random
import time
import physics_objects as pho

def main():
    """This is a bouncing ball game"""
    win = gr.GraphWin("Bouncing Ball Game", 500, 500, False)
    win.setBackground ('orange')
    # create a ball
    ball = pho.Ball(win)
    # move it to the center of the screen and draw it
    ball.setPosition(25, 25)
    # give it a random velocity
    ball.setVelocity(random.uniform(-5, 5), random.uniform(-5, 5))
    # set the acceleration to (0, -20)
    ball.setAcceleration(0, -20)
    # set ball color to blue
    c = [0, 0, 255]
    #ball.setColor(c)
    ball.draw()

    #create a block 
    block = pho.Block( win, dx = 6, dy = 3 )
    block.setPosition(25, 0)
    # set block color to blue
    c = [0, 0, 255]
    block.setColor(c)
    block.draw()
    
    # number of hits
    hits = 0
    textbox = gr.Text( gr.Point( 250, 50 ), "Number of hits: " + str(hits) )

    while True:
        # call the ball's update method with a dt of 0.033
        ball.update(0.033)
        time.sleep( 0.033 ) # have the animation go at the same speed

        p = ball.getPosition()
        print( 'Position:', p[0], p[1])

        v = ball.getVelocity()
        print( 'Velocity:', v[0], v[1])

        input = win.checkKey()

        if input == 'q': # did the user type a 'q'?
            break
        
        if input == 'a':
        # move the block to the left
            block.setPosition( (block.getPosition()[0] - 2), 0)
        
        if input == 'd':
        # move the block to the right
            block.setPosition( (block.getPosition()[0] + 2), 0)

        
        if win.checkMouse(): # did the user click the mouse?
            break

        # if the ball is outside the window
        (posx, posy) = ball.getPosition()
        if posx > 50 or posx < 0 or posy > 50 or posy < 0: 
           # reposition the ball to the center of the window
           ball.setPosition(25, 25)
           # give it a random velocity
           ball.setVelocity(random.uniform (-5, 5), random.uniform(-5, 5))


        if block.collision(ball) == True:
            # if the ball hits the block, bounce
            ball.setVelocity(ball.getVelocity()[0], - ball.getVelocity()[1])
            # change the ball to a random color
            c = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
            ball.setColor(c)
            hits += 1
            # update the hit number
            textbox.undraw()
            textbox = gr.Text( gr.Point( 250, 50 ), "Number of hits: " + str(hits) )
            textbox.draw(win)


    # win.getMouse()
            win.update()
    win.close()

if __name__ == "__main__":
    main()

