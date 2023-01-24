from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Verdana', 15, 'bold')


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0          
        with open("C:/Users/Pratik.DESKTOP-FG3O5CT/Desktop/data.txt") as file:
            self.high_score=int(file.read())
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(0, 280)
        self.score_write()

    def score_update(self):
        self.score += 1

    def reset(self):
        if (self.score > self.high_score):
            self.high_score = self.score
        self.score = 0
        self.score_write()
        with open("C:/Users/Pratik.DESKTOP-FG3O5CT/Desktop/data.txt",'w') as file:
            file.write(str(self.high_score))
    
    
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER!",False,ALIGNMENT,FONT)

    def score_write(self):
        self.clear()
        self.write(
            f"Score:{self.score}  High Score:{self.high_score}", False, ALIGNMENT, FONT)
