from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Verdana', 15, 'bold')


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(0, 280)
        self.score_write()

    def score_update(self):
        self.score += 1

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!",False,ALIGNMENT,FONT)

    def score_write(self):
        self.clear()
        self.write(f"Score:{self.score}", False, ALIGNMENT, FONT)
