



















count_loops = 0
game_is_on = 1
while game_is_on:
    time.sleep(0.1)
    screen.update()
    count_loops += 1

    # TODO 2. Cars are randomly generated along the y-axis and
    #  will move from the right edge of the screen to the left edge.
    if count_loops == 6:
        car = CarManager()
        count_loops = 0
    if car_fleet:
        for cars in car_fleet:
            cars.move()

    # TODO 3. When the turtle hits the top edge of the screen,
    #  it moves back to the original position and the player levels up.
    #  On the next level, the car speed increases.
    if turtle_j.ycor() > 290:
        turtle_j.reset_position()
        scoreboard.increase_score()
        for cars in car_fleet:
            cars.increase_level()


screen.exitonclick()
