import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600, startx=0, starty=0)
screen.tracer(0)

# TODO 1: 1. A turtle moves forwards when you press the "Up" key.
#  It can only move forwards, not back, left or right.
turtle_j = Player()

screen.listen()
screen.onkey(fun=turtle_j.move_forward, key="Up")

scoreboard = Scoreboard()

car_fleet = CarManager()

game_is_on = 1
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # TODO 2. Cars are randomly generated along the y-axis and
    #  will move from the right edge of the screen to the left edge.
    car_fleet.create_car()
    car_fleet.move()

    # TODO 4. When the turtle collides with a car, it's game over
    #  and everything stops.
    for car in car_fleet.car_fleet:
        if car.distance(turtle_j) < 20:
            game_is_on = 0
            scoreboard.game_over()

    # TODO 3. When the turtle hits the top edge of the screen,
    #  it moves back to the original position and the player levels up.
    #  On the next level, the car speed increases.
    if turtle_j.at_finish_line():
        turtle_j.reset_position()
        scoreboard.increase_score()
        car_fleet.increase_level()


screen.exitonclick()







