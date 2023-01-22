from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__('circle')
        self.color('white')
        self.penup()
        # self.shape('circle')
        self.setheading(0)
        self.move()
        self.movement=0.1


    def move(self):
        self.forward(20)

    def change_direction(self,degree):
        self.setheading(degree)
    
    def change_moment(self):
        self.movement*=0.9

    def reset(self,degree):
        self.goto(0,0)
        self.movement=0.1
        self.change_direction(degree)
