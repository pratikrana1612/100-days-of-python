from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__('circle')
        self.color('white')
        self.penup()
        # self.shape('circle')
        self.setheading(0)
        self.move()


    def move(self):
        self.forward(20)

    def change_direction(self,degree):
        self.setheading(degree)

