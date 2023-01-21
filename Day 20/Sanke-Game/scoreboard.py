from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(0,280)
        self.score_write()
    
    def score_update(self):
        self.score+=1

    def score_write(self):
        self.clear()
        self.write(f"Score:{self.score}",False,'center',('Verdana',15,'bold'))
