from turtle import Turtle
from random import randint

SCREEN_LIMIT_POSITIVE = 280
SCREEN_LIMIT_NEGATIVE = -280
STRETCHING = 0.5


class Food(Turtle):
    # todo 1: create a circle in the screen, the circle is the food
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=STRETCHING, stretch_len=STRETCHING)
        self.penup()
        self.color("purple")
        self.refresh()

    # todo 2: when the snake touches the food, it goes to a new random location
    def refresh(self):
        x_coord = randint(SCREEN_LIMIT_NEGATIVE, SCREEN_LIMIT_POSITIVE)
        y_coord = randint(SCREEN_LIMIT_NEGATIVE, SCREEN_LIMIT_POSITIVE)
        self.goto(x=x_coord, y=y_coord)

