from random import choice, randint
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
MAXIMUM_CARS=25
# how is this working even if i am creating car a some and editing at some other place


class CarManager():
    def __init__(self):
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE
        for _ in range(randint(1, MAXIMUM_CARS)):
            car = Turtle('square')
            self.create(car)
            self.cars.append(car)

    def create(self, car):
        car.penup()
        car.color(choice(COLORS))
        car.shapesize(1, 2)
        self.position(car)
        car.setheading(180)

    def position(self, car):
        car.goto(randint(300, 600), randint(-300, 300))

    def moving(self):
        for car in self.cars:
            car.forward(self.speed)
            if (car.xcor() < -300):
                self.position(car)

    def increae_speed(self):
        self.speed += MOVE_INCREMENT
