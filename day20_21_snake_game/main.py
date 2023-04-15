# Standards
from turtle import Screen
from time import sleep

# My own
from snake import Snake
from food import Food
from scoreboard import Scoreboard


DISTANCE_TO_COLLIDE = 16
NORTH_EAST_LIMIT = 295
SOUTH_WEST_LIMIT = -295


# preparing the screen for the animation
screen = Screen()
screen.setup(width=600, height=600, startx=550, starty=0)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

# TODO 1: Create a snake body
snake = Snake()

# TODO 3: Create snake food
food = Food()

# TODO 5: Create a scoreboard
score = Scoreboard()


screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")


# want_to_play = screen.textinput("Play again?", "Type 'y' for yes and 'n' for no. ")
# if want_to_play == "y":
#     return 1
# else:
#     return 0


# TODO 2: Move the snake
is_moving = 1
while is_moving:
    # video 187, time 10.23 provides summary
    # my job is tWhat your job needs to be is to understand how things work.
    # Make sure that you understand how to use the code,
    # when to use it, how it works behind the scenes.
    screen.update()
    sleep(0.1)
    snake.move()

    # TODO 4: Detect collision with food
    if snake.head.distance(food) < DISTANCE_TO_COLLIDE:
        food.refresh()
        snake.extend()
        score.increase_score()
        score.show_it()

    # TODO 6: Detect collision with wall
    pos_x = snake.head.pos()[0]
    pos_y = snake.head.pos()[1]
    if pos_x >= NORTH_EAST_LIMIT or pos_x <= SOUTH_WEST_LIMIT \
            or pos_y >= NORTH_EAST_LIMIT or pos_y <= SOUTH_WEST_LIMIT:
        score.reset()
        snake.reset()
        # is_moving = score.finish_message()

    # TODO 7: Detect collision with tail
    for part in snake.snake_parts[1:]:
        if snake.head.distance(part) < 10:
            score.reset()
            snake.reset()
            # is_moving = score.finish_message()

screen.exitonclick()
