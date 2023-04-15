from turtle import Turtle, Screen
from time import sleep

POSITION = (-30, 230)
POSITION_FINAL = (-45, 0)
ALIGNMENT = "center"
screen = Screen()


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.read_score_file()
        self.penup()
        self.color("white")
        self.goto(POSITION)
        self.ht()
        self.show_it()

    def show_it(self):
        self.clear()
        self.write(f"Score: {self.score}\nHigh Score: {self.high_score}", align=ALIGNMENT)

    def write_score_file(self):
        with open(r"highest_score.txt", mode="w") as file:
            file.write(f"{self.high_score}")

    def read_score_file(self):
        ''' Read data from .txt file. An integer is expected. '''
        with open("highest_score.txt", mode="r") as file:
            contents = int(file.read())
        return contents

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_score_file()
        self.score = 0
        self.show_it()

    def increase_score(self):
        self.score += 1

    # def finish_message(self):
    #     self.goto(POSITION_FINAL)
    #     self.clear()
    #     self.write(f"GAME OVER.\nYour score is: {self.score}."
    #                f"The highest score is: {self.high_score}", align=ALIGNMENT)
    #     sleep(3)
    #     self.clear()

