from turtle import Turtle

MOVING_STEP = 10
INITIAL_REFRESH = 0.1


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("white")
        self.x_move = 10
        self.y_move = 10
        self.refresh_time = INITIAL_REFRESH

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1

    def hit(self):
        self.x_move *= -1
        self.refresh_time *= 0.6

    def reset_position(self):
        self.goto(0, 0)
        self.hit()
        self.refresh_time = INITIAL_REFRESH


