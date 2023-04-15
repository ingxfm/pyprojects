from turtle import Turtle

FONT = ("Courier", 20, "normal")
ALIGNMENT = "center"
INITIAL_POSITION = (-200, 260)


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 1
        self.ht()
        self.color("black")
        self.penup()
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(INITIAL_POSITION)
        self.write(f"Level {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
