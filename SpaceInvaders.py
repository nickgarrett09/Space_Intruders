# Space Invaders!
# Nick Garrett
# May 9, 2018

# Python Game Programming Tutorial: Space Invaders
# Christian Thompson

import turtle
import os
import math
import random
from time import sleep

# Create game over varialbe
isGameOver = 0

# Create screen
wn = turtle.Screen()
wn.bgcolor("Black")
wn.title("Space Invaders")
wn.bgpic("space_invaders_background.gif")

# register the Shapes
wn.register_shape("invader.gif")
wn.register_shape("player.gif")

# Draw Border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pensize(3)
border_pen.pendown()
border_pen.hideturtle()
for i in range(4):
    border_pen.fd(600)
    border_pen.lt(90)

#Set the score to 0
score = 0
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290,260)
scorestring = "Score: %s" %score
score_pen.write(scorestring, False, align="left", font=("Arial", 20, "normal"))
score_pen.hideturtle()

# Create Player
player = turtle.Turtle()
player.shape("player.gif")
player.color("blue")
player.lt(90)
player.penup()
player.setposition(0,-250)
player.speed(0)

playerspeed = 15

# Create the player's bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.lt(90)
bullet.shapesize(0.5,0.5)
bullet.hideturtle()

bulletspeed = 25

# Define bullet state
# ready - ready to fire
# fire - bullet is firing
bulletstate = "ready"



# choose a number of enemies
number_if_enemies = 5
# Create an empty list of enemies
enemies = []

# add enemies to the list
for i in range(number_if_enemies):
    # Create the enemy
    enemies.append(turtle.Turtle())

for enemy in enemies:
    enemy.color("red")
    enemy.shape("invader.gif")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200,200)
    y = random.randint(200, 270)
    enemy.setposition(x,y)

enemyspeed = 2

# Player Movements
def move_left():
    x = player.xcor() - playerspeed
    if x < -280:
        x = -280
    player.setx(x)
    
def move_right():
    x = player.xcor() + playerspeed
    if x > 280:
        x = 280
    player.setx(x)
    
def fire_bullet():
    # Declare bullet state as a global if it needs changed
    global bulletstate 
    if bulletstate == "ready":
        os.system("aplay laser.wav&")
        bulletstate = "fire"
        # Move bullet just above the player
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x,y)
        bullet.showturtle()

def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 25:
        return True
    else:
        return False


# Create keyboard bindings
wn.listen()
wn.onkey(move_left, "Left")
wn.onkey(move_right, "Right")
wn.onkey(fire_bullet, "space")

# Main Game Loop
while True:

    for enemy in enemies:

        # Move the enemy
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)

        # Move the enemy back and down
        if enemy.xcor() > 280 or enemy.xcor() < -280:
            # Moves all enemies down
            for e in enemies:
                y = e.ycor()
                y -= 30
                e.sety(y)
            # Change enemy direction    
            enemyspeed *= -1
                

        # check for the collision between the bullet and the enemy
        if isCollision(bullet,enemy):
            os.system("aplay explosion.wav&")
            # reset the bullet
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0,-400)
            # Reset the enemy
            enemy.setposition(random.randint(-200,200), 275)
            # update the score
            score += 10
            scorestring = "Score: %s" %score
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Arial", 20, "normal"))
            # Increase enemy speed
            if enemyspeed > 0:
                enemyspeed += 3
            else:
                enemyspeed -= 3

        if isCollision(player,enemy):
            os.system("aplay explosion.wav&")
            isGameOver = 1
            break
        
        # End game if invaders reach earth
        if enemy.ycor() < -300:
            isGameOver = 1    

    #Break the Loop
    if isGameOver == 1:
        player.hideturtle()
        bullet.hideturtle()
        for e in enemies:
            e.hideturtle()
        score_pen.setposition(-100,-20)
        score_pen.write("GAME OVER", False, align="left", font=("Arial", 40, "normal"))
        print("Game Over")
        for i in range(5):
            os.system("aplay explosion.wav&")
            sleep(.5)
        break
    # Move the bullet
    if bulletstate == 'fire':
        y  = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

    # Check to see if the bullet has reached the top
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"

    



delay = input("Press Enter to Finish")