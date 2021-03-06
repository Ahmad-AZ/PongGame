# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import turtle
window = turtle.Screen() # creating window
window.title("simple pong Game ->")
window.bgcolor("black")
window.setup(width=700, height=700)
window.tracer(0)   #  showing  screen while drawing

# Paddle 1
paddle_1 = turtle.Turtle()  # by defult 20 width and 20 px height
paddle_1.speed(0) #turtle's speed
paddle_1.shape("square")
paddle_1.color("red")
paddle_1.shapesize(stretch_wid=5,stretch_len=1)  # 5*20px width
paddle_1.penup() #--------
paddle_1.goto(-320,0) #--------


# Paddle 2
paddle_2 = turtle.Turtle()  # by defult 20 width and 20 px height
paddle_2.speed(0) #turtle's speed
paddle_2.shape("square")
paddle_2.color("red")
paddle_2.shapesize(stretch_wid=5,stretch_len=1)  # 5*20px width
paddle_2.penup()
paddle_2.goto(320,-0) #--------


# Ball
ball = turtle.Turtle()  # by defult 20 width and 20 px height
ball.speed(0) #turtle's speed
ball.shape("circle")
ball.color("white")
ball.pencolor('white')
ball.goto(0,0) #-------
ball.dx=0.4 # it moves every time by two pixels
ball.dy=0.4



def paddle_1_up():
    y = paddle_1.ycor() # return the y coordinate
    y+=40
    paddle_1.sety(y)

    if y > 300 :
       y = 300
    paddle_1.sety(y)


def paddle_1_down():
    y = paddle_1.ycor() # return the y coordinate
    y-=40
    if y < -300:
       y = -300
    paddle_1.sety(y)



def paddle_2_up():
    y = paddle_2.ycor() # return the y coordinate
    y+=40
    if y > 300:
        y= 300
    paddle_2.sety(y)


def paddle_2_down():
    y = paddle_2.ycor() # return the y coordinate
    y-=40
    if y < -300:
        y= -300
    paddle_2.sety(y)





# keyboard binding
window.listen() # listen to the keyboard input
window.onkeypress( paddle_1_up ,"w")
window.onkeypress( paddle_1_down ,"s")

window.onkeypress( paddle_2_up ,"Up")
window.onkeypress( paddle_2_down ,"Down")





while True:
    window.update() # updating the screen and keep it running
    # move the  ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    # border checking
    if ball.ycor() > 340:
        ball.sety(340)
        ball.dy *=-1 # reverse the direction


    if ball.ycor() < -340:
        ball.sety(-340)
        ball.dy *= -1 # reverse the direction


    if ball.xcor() > 340:
        ball.goto(0,0)
        ball.dx *=-1

    if ball.xcor() < -340:
        ball.goto(0,0)
        ball.dx *=-1

# paddle and ball coalitions
    if (ball.xcor() > 300 and ball.xcor() < 320) and (ball.ycor() < paddle_2.ycor() +
                              40 and ball.ycor() > paddle_2.ycor() -40 ):
        ball.setx(300)
        ball.dx *= -1


    if (ball.xcor() < -300 and ball.xcor() > -320) and (ball.ycor() < paddle_1.ycor() +
                              40 and ball.ycor() > paddle_1.ycor() -40 ):
        ball.setx(-300)
        ball.dx *= -1