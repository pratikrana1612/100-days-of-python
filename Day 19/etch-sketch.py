from turtle import Turtle,Screen


timmy = Turtle()
screen=Screen()

screen.listen()

def timmy_forward():
    timmy.forward(50)
def timmy_backward():
    timmy.backward(50)
def timmy_right():
    timmy.right(30)
    timmy.forward(30)
def timmy_left():
    timmy.left(30)
    timmy.forward(30)
def timmy_clear():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()

screen.onkey(key='w',fun=timmy_forward)
screen.onkey(key='s',fun=timmy_backward)
screen.onkey(key='d',fun=timmy_right)
screen.onkey(key='a',fun=timmy_left)
screen.onkey(key='c',fun=timmy_clear)



screen.exitonclick()