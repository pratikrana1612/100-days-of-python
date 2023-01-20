# from turtle import Screen, Turtle
from turtle import Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("My Snake Game")

snake=Snake()
# timmy = Turtle
game_is_on = True
while game_is_on:
    snake.move()
    # turtles[0].left(90)

screen.exitonclick()
