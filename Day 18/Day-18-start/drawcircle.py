from turtle import Screen
from turtle import Turtle as T
from random import randint,choice

timmy=T()
screen=Screen()
screen.colormode(255)
timmy.speed('fastest')
# timmy.width(3)
def randomcolor():
    return (randint(0,255),randint(0,255),randint(0,255))

def drawCircle(gap):
    for _ in range(int(360/gap)):
        timmy.color(randomcolor())
        timmy.circle(100)
        position=timmy.heading()
        timmy.setheading(position+gap)

# timmy.circle(100)
drawCircle(5)
















screen.exitonclick()