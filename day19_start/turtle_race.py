from turtle import Turtle, Screen
from random import randint

is_race_ON = 0  # False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet!",
                            prompt="Which turtle will win? Enter a color: "
                                   "List: red, orange, yellow, green, blue, purple")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
x_coord = -235
y_coord = [-75, -45, -15, 15, 45, 75]

turtles = []
for coloring in colors:
    i = colors.index(coloring)
    turtle = Turtle(shape="turtle")
    turtle.color(coloring)
    turtle.penup()
    turtle.setposition(x=x_coord, y=y_coord[i])
    turtles.append(turtle)

if user_bet:
    is_race_ON = 1  # True

while is_race_ON:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_ON = 0
            if turtle.pencolor() == user_bet:
                print(f"You won. The winner is the {turtle.pencolor()} turtle.")
            else:
                print(f"You lost. The winner is the {turtle.pencolor()} turtle.")
        else:
            movement = randint(0, 10)
            turtle.forward(movement)
# TODO 8: move each turtle


# TODO 6: maintain the screen without disappearing while drawing
# TODO 7: turn off the game
screen.exitonclick()