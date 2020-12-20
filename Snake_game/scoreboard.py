from turtle import Turtle

INITIAL_SCORE = 0
INITIAL_X = 0
INITIAL_Y = 310

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = INITIAL_SCORE
        self.penup()
        self.goto(INITIAL_X, INITIAL_Y)
        self.pendown()
        self.refresh()
        self.color("white")
        
        
    def refresh(self):
        self.write(('SCORE: ', self.update_score()), font=("Arial", 18, "normal"))
        self.hideturtle()

    def update_score(self):
        self.score += 1
        return self.score