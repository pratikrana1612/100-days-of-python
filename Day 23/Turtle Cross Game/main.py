import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
score = Scoreboard()
car = CarManager()
screen.listen()
screen.onkey(player.move, 'Up')
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.moving()
    if (player.ycor() > 280):
        score.increase_score()
        car.increae_speed()
        player.reset()
    for i in car.cars:
        if (i.distance(player) < 20):
            score.game_over()
            screen.update()
            time.sleep(1)
            game_is_on = False
