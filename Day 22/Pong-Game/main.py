from turtle import Screen, Turtle
from random import randint
from paddle import Paddle
from user import User
from ball import Ball
import time
screen = Screen()
# screen.screensize(800,600,'black')
screen.setup(800, 600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

left_paddle = Paddle((-350, 0))
right_paddle = Paddle((350, 0))
user_1=User((100,250))
user_2=User((-100,250))
ball = Ball()
# screen.update()

# paddle.left(30)
screen.listen()
screen.onkey(right_paddle.up_control, 'Up')
screen.onkey(right_paddle.down_control, 'Down')
screen.onkey(left_paddle.down_control, 's')
screen.onkey(left_paddle.up_control, 'w')

game_on = True
screen.update()
while game_on:
    ball.move()
    time.sleep(ball.movement)
    screen.update()
    if (ball.ycor() > 280):
        ball.change_direction(randint(260, 320))
    elif (ball.ycor() < -280):
        ball.change_direction(randint(45, 110))
    if ((ball.xcor() > 300 and ball.distance(right_paddle) < 30)):
        # print("make contact")
        # ball.setheading(200)
        ball.change_direction(randint(90, 270))
        ball.change_moment()
        # ball.change_direction(randint(60,300))
    elif (ball.xcor() < -300 and ball.distance(left_paddle) < 30):
        # ball.setheading(-290)
        # ball.setheading(70)
        ball.change_direction(randint(-90, 90))
        ball.change_moment()
        # ball.change_direction(300)
    if(ball.xcor()>400):
        ball.reset(180)
        user_2.score_increase()
        screen.update()
    elif(ball.xcor()<-400):
        ball.reset(0)
        user_1.score_increase()
        screen.update()


screen.exitonclick()
