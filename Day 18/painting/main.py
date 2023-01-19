from turtle import Turtle,Screen
from random import choice
#  import colorgram
#
# colors=colorgram.extract('paintImage.jpg',30)
#
# rgb_colors=[]
# for color in colors:
#     tuple=(color.rgb.r,color.rgb.g,color.rgb.b)
#     rgb_colors.append(tuple)
#
# print(rgb_colors)
screen=Screen()
screen.colormode(255)
color_list = [(232, 241, 239), (1, 9, 30), (229, 235, 242), (239, 232, 238), (121, 95, 41), (72, 32, 21),
              (238, 212, 72), (220, 81, 59), (226, 117, 100)]
            

timmy=Turtle()
timmy.speed('fastest')
timmy.hideturtle()
# timmy.dot(20,(1, 9, 30))
timmy.penup()
width=-275
height=-200
timmy.goto(width,height)
for _ in range(10):
    for _ in range(10):
        timmy.dot(20,choice(color_list))
        timmy.forward(50)
    height+=50
    timmy.goto(width,height)
# print(screen.screensize())

screen.exitonclick()

