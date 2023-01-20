from turtle import Screen, Turtle
import time

screen=Screen()
screen.tracer(0)
class Snake:
    def __init__(self):
        self.turtles = []
        x_cordinate = 0
        for _ in range(3):
            new_turtle = Turtle('square')
            new_turtle.color('white')
            new_turtle.penup()
            new_turtle.goto(x_cordinate, 0)
            self.turtles.append(new_turtle)
            x_cordinate -= 20
    screen.update()

    def move(self):
        for i in range(len(self.turtles)-1,0,-1):
                # turtle=self.turtles[1]
                position=self.turtles[i-1].pos()
                self.turtles[i].goto(position)
                # screen.update()
        self.turtles[0].forward(20)
        time.sleep(0.1)
        screen.update() 