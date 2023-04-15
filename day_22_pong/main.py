# Built-in
from turtle import Turtle, Screen
from time import sleep
from random import randint

# My own
from racket import Racket
from ball import Ball
from scoreboard import Scoreboard

START_LINE_POS = (0, -280)
DRAW_LINE = 300
SPACING_DASHED_LINE = 10
ANGLE_UP = 90
PLAYER_RIGHT_START_POS = (380, 0)
PLAYER_LEFT_START_POS = (-385, 0)
WALL_LIMITS = 283
OUT_OF_BOUNDS = 380
HEADING = 35

# TODO 1: Create a screen with a line in the middle
screen = Screen()
screen.setup(width=800, height=600, startx=0, starty=0)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# Line in screen
line = Turtle()
line.penup()
line.color("white")
line.goto(START_LINE_POS)
line.left(ANGLE_UP)
for _ in range(int(DRAW_LINE/SPACING_DASHED_LINE)):
    line.pendown()
    line.forward(SPACING_DASHED_LINE)
    line.penup()
    line.forward(SPACING_DASHED_LINE)
line.hideturtle()

# TODO 2: Create a racket and move it
screen.listen()
player1 = Racket()
player1.start_position(PLAYER_RIGHT_START_POS)
screen.onkey(fun=player1.up, key="Up")
screen.onkey(fun=player1.down, key="Down")


# TODO 3: Create a 2nd racket and move it
player2 = Racket()
player2.start_position(PLAYER_LEFT_START_POS)
screen.onkey(fun=player2.up, key="w")
screen.onkey(fun=player2.down, key="s")


# TODO 4: Create a ball and make it move
ball = Ball()

# TODO 5: Scores
scoreboard = Scoreboard()

is_moving = 1
while is_moving:
    screen.update()
    sleep(ball.refresh_time)
    ball.move()

    # collision with wall
    if ball.ycor() > WALL_LIMITS or ball.ycor() < -WALL_LIMITS:
        # subtract instead of adding the MOVING_STEP
        ball.bounce()

    # collision with paddle
    if ball.distance(player1) < 50 and ball.xcor() > 350 or ball.distance(player2) < 50 and ball.xcor() < -350:
        ball.hit()

    if ball.xcor() > OUT_OF_BOUNDS:
        scoreboard.left_score()
        ball.reset_position()
        # is_moving = 0

    if ball.xcor() < -OUT_OF_BOUNDS:
        scoreboard.right_score()
        ball.reset_position()
        # is_moving = 0

screen.exitonclick()
