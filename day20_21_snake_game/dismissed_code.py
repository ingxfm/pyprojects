''' my class before learning from my mentor
from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x=new_x, y=new_y)
        self.segments[0].forward(MOVE_DISTANCE)
'''


''' Old code without classes
from turtle import Screen, Turtle
from random import randint
from time import sleep
from snake import Snake

# preparing the screen for the animation
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

# TODO 1: Create a snake body
# snake_parts = []
# for snake_part in range(3):
#     s_part = Turtle(shape="square")
#     s_part.color("white")
#     s_part.penup()
#     s_part.goto(x=-20*snake_part, y=0)
#     snake_parts.append(s_part)
snake = Snake()
print(snake)


# TODO 3: Create snake food
# food = Turtle(shape="square")
# food.penup()
# food.color("purple")
# x_coord = randint(-100, 100)
# y_coord = randint(-100, 100)

# # TODO 2: Move the snake
# is_moving = 1
# while is_moving:
#     screen.update()
#     sleep(1)
#     for part_num in range(len(snake_parts) - 1, 0, -1):
#         new_x = snake_parts[part_num - 1].xcor()
#         new_y = snake_parts[part_num - 1].ycor()
#         snake_parts[part_num].goto(x=new_x, y=new_y)
#     snake_parts[0].forward(20)
#     snake_parts[0].left(90)

is_moving = 1
while is_moving:
    screen.update()
    sleep(1)
    snake.move()



# TODO 4: Detect collision with food
# TODO 5: Create a scoreboard
# TODO 6: Detect collision with wall

# TODO 7: Detect collision with tail
screen.exitonclick()

'''

from turtle import Turtle

igual = Turtle()

print(igual.pos()[0])
