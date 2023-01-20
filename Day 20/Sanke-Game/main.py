# from turtle import Screen, Turtle
from turtle import Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("My Snake Game")
screen.tracer(0)
snake = Snake()
screen.update()

screen.listen()
screen.onkey(snake.snake_up, "Up")
screen.onkey(snake.snake_down, "Down")
screen.onkey(snake.snake_left, "Left")
screen.onkey(snake.snake_right, "Right")
# timmy = Turtle()
game_is_on = True
while game_is_on:
    snake.move()
    time.sleep(0.1)
    screen.update()
    # turtles[0].left(90)

screen.exitonclick()
