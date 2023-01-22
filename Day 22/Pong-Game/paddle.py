from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, pos):
        super().__init__('square')
        self.create(pos)

    def create(self, pos):
        # paddle = Turtle('square')
        self.penup()
        self.color('white')
        self.shapesize(1, 5)
        self.setheading(90)
        self.goto(pos)
        self.speed('fastest')

    def up_control(self):
        self.forward(20)
        # screen.update()

    def down_control(self):
        self.backward(20)
        # screen.update()
