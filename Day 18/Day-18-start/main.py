from turtle import Screen
from turtle import Turtle
from random import randint

timmy = Turtle()
timmy.shape("turtle")
# import heroes
# timmy.color("red")
# for i in range(1,5):
#     timmy.forward(100)
#     timmy.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# for i in range(15):
#     timmy.pendown()
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
# if(i%2==0):
#     timmy.penup()
# else:
#     timmy.pendown()
# timmy.forward(10)
screen = Screen()
degree = 3
screen.colormode(255)


for i in range(7):
    for j in range(0, degree):
        timmy.forward(100)
        timmy.right(360 / degree)
    degree += 1
    timmy.color(randint(1, 255), randint(1, 255), randint(1, 255))
    # timmy.color(f'{randint(1,255)},{randint(1,255)},{randint(1,255)}')
    # color=str(round(uniform(1,255),2))
    # timmy.pencolor()
    # timmy.pencolor(f'{color},{color},{color}')

    # timmy.forward(100)
    # timmy.right(120)
    # timmy.forward(100)
    # timmy.right(120)
    # timmy.forward(100)
    # timmy.right(120)
    # timmy.forward(100)
    # print(uniform(1.0, 255.0))

screen.exitonclick()
