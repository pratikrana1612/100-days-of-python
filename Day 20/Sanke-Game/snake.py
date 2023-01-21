from turtle import Screen, Turtle

DISTANCE_COVER = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.turtles = []
        self.create()

    def create(self):
        x_cordinate = 0
        for _ in range(3):
            new_turtle = Turtle('square')
            new_turtle.color('white')
            new_turtle.penup()
            new_turtle.goto(x_cordinate, 0)
            self.turtles.append(new_turtle)
            x_cordinate -= 20

    def move(self):
        for i in range(len(self.turtles)-1, 0, -1):
            # turtle=self.turtles[1]
            position = self.turtles[i-1].pos()
            self.turtles[i].goto(position)
            # screen.update()
        self.turtles[0].forward(DISTANCE_COVER)

    def snake_up(self):
        if self.turtles[0].heading() != DOWN:
            self.turtles[0].setheading(90)

    def snake_down(self):
        if self.turtles[0].heading() != UP:
            self.turtles[0].setheading(270)

    def snake_left(self):
        if self.turtles[0].heading() != RIGHT:
            self.turtles[0].setheading(180)

    def snake_right(self):
        if self.turtles[0].heading() != RIGHT:
            self.turtles[0].setheading(0)
