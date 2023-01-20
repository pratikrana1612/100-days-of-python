from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.colormode(255)
screen.setup(width=500, height=400)
turtles = []
user_bet = screen.textinput(
    "Make your bet?", "which turtle will win the race?Enter a color:"
)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]



def make_turtle(x, y, color):
    timmy = Turtle(shape="turtle")
    timmy.penup()
    timmy.color(color)
    timmy.goto(x=x, y=y)
    turtles.append(timmy)


x = -240
y = -100
for i in range(6):
    make_turtle(x, y, colors[i])
    y += 25

# t=Turtle()
# print(t.pos()[0])
def winner(user_choice, winner):
    if user_choice == winner:
        print(f"You've won! The {winner} turtle is winner!")
    else:
        print(f"You've lost! The {winner} turtle is winner!")


race_is_on = True
while race_is_on:
    for turtel in turtles:
        move = randint(1, 10)
        turtel.forward(move)
        # print(turtel.pos())
        if turtel.pos()[0] >= 230:
            winner(user_bet, turtel.pencolor())
            race_is_on = False

# timmy.penup()
# timmy.shape('turtle')
# timmy.goto(x=125,y=100)


screen.exitonclick()
