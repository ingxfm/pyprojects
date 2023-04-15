from turtle import Turtle
from random import randint, choice

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
START_X = 290


class CarManager:

    def __init__(self):
        self.car_fleet = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = randint(1, 6)
        if random_chance == 1:
            new_car = Turtle(shape="square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(choice(COLORS))
            new_car.penup()
            new_car.goto(x=START_X, y=randint(-230, 250))
            self.car_fleet.append(new_car)

    def move(self):
        for car in self.car_fleet:
            car.backward(self.car_speed)

    def increase_level(self):
        self.car_speed += MOVE_INCREMENT
