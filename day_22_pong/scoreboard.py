from turtle import Turtle, Screen

ALIGNMENT = "center"
FONT = ("Arial", 70, "normal")
POS_SCORE_PLAYER_1 = (-90, 200)
POS_SCORE_PLAYER_2 = (90, 200)


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score_right_player = 0
        self.score_left_player = 0
        self.penup()
        self.color("red")
        self.ht()
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(POS_SCORE_PLAYER_1)
        self.write(self.score_left_player, align=ALIGNMENT, font=FONT)
        self.goto(POS_SCORE_PLAYER_2)
        self.write(self.score_right_player, align=ALIGNMENT, font=FONT)

    def right_score(self):
        self.score_right_player += 1
        self.update_score()

    def left_score(self):
        self.score_left_player += 1
        self.update_score()
