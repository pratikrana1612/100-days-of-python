from turtle import Screen, Turtle
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("My Snake Game")
screen.tracer(0)
snake = Snake()
food = Food()
score = Score()
screen.update()

screen.listen()
screen.onkey(snake.snake_up, "Up")
screen.onkey(snake.snake_down, "Down")
screen.onkey(snake.snake_left, "Left")
screen.onkey(snake.snake_right, "Right")
screen.onkey(snake.hack,'l')
# timmy = Turtle()
# timmy.xcor()
game_is_on = True
while game_is_on:
    snake.move()
    time.sleep(0.1)
    screen.update()
    if snake.turtles[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        score.score_update()
        score.score_write()
    for sanke_part in snake.turtles[1:]:
        # if (sanke_part == snake.turtles[0]):
        #     pass
        if (snake.turtles[0].distance(sanke_part) < 10):
            game_is_on = False
            # score.game_over()
    if snake.turtles[0].xcor() > 278 or snake.turtles[0].xcor() < -278 or snake.turtles[0].ycor() > 278 or snake.turtles[0].ycor() < -278:
        score.reset()
        game_is_on = False
        # score.game_over()
    # turtles[0].left(90)

screen.exitonclick()
