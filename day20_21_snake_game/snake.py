from turtle import Turtle

MOVE_DISTANCE = 20
NORTH = 90
SOUTH = 270
EAST = 0
WEST = 180
INITIAL_LENGTH = 3
INITIAL_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:

    def __init__(self):
        self.snake_parts = []
        self.create_snake()
        self.head = self.snake_parts[0]

    def add_part(self, position):
        new_part = Turtle(shape="square")
        new_part.color("white")
        new_part.penup()
        new_part.goto(position)
        self.snake_parts.append(new_part)

    def create_snake(self):
        for position in INITIAL_POSITIONS:
            self.add_part(position)

    def extend(self):
        self.add_part(self.snake_parts[-1].pos())

    def reset(self):
        for part in self.snake_parts:
            part.goto(1000, 1000)
        self.snake_parts.clear()
        self.create_snake()
        self.head = self.snake_parts[0]

    def move(self):
        for part_num in range(len(self.snake_parts) - 1, 0, -1):
            new_x = self.snake_parts[part_num - 1].xcor()
            new_y = self.snake_parts[part_num - 1].ycor()
            self.snake_parts[part_num].goto(x=new_x, y=new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != SOUTH:
            self.head.setheading(NORTH)

    def down(self):
        if self.head.heading() != NORTH:
            self.head.setheading(SOUTH)

    def right(self):
        if self.head.heading() != WEST:
            self.head.setheading(EAST)

    def left(self):
        if self.head.heading() != EAST:
            self.head.setheading(WEST)