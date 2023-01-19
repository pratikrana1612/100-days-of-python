from turtle import Screen
from turtle import Turtle as T
from random import randint,choice

timmy=T()
timmy.width(15)
timmy.speed(7)
directions=[0,90,270,360]
# walk=['forward','backward','right','left']
# walk=[timmy.forward,timmy.backward,timmy.left,timmy.right]
# timmy.choice(walk)()
# timmy.way()

screen=Screen()
screen.colormode(255)
# T.colormode(255)

for _ in range(1,150):
    timmy.color(randint(1,255),randint(1,255),randint(1,255))
    timmy.setheading(choice(directions))
    timmy.forward(30)
    # number=randint(1,4)
    # if(number==1):
    #     timmy.forward(40)
    # elif(number==2):
    #     timmy.backward(40)
    # elif(number==3):
    #     timmy.right(40)
    # else:
    #     timmy.left(40)



screen.exitonclick()