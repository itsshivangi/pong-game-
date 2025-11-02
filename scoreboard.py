from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("DarkBlue")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.goto(-100,200)
        self.write(f"{self.l_score}  {self.r_score}", align="center", font=("Courier", 24, "normal"))

    