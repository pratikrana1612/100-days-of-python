from turtle import Turtle


class User(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(position)
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f'{self.score}', False, 'center', ('Verdana', 24, 'bold'))

    def score_increase(self):
        self.score += 1
        self.update_score()
