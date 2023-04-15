from turtle import Turtle

MOVING_STEP = 20
RACKET_LEN = 5
RACKET_WID = 1


class Racket(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=RACKET_WID, stretch_len=RACKET_LEN)
        self.left(90)
        self.penup()
        self.color("white")

    def start_position(self, position):
        self.goto(position)

    def up(self):
        self.forward(MOVING_STEP)

    def down(self):
        self.backward(MOVING_STEP)
