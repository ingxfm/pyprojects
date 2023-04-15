import turtle as turtle_module


leonardo = turtle_module.Turtle()
screen = turtle_module.Screen()


# TODO 1: W to go forwards
def move_forwards():
    leonardo.forward(10)


# TODO 2: S to go backwards
def move_backwards():
    leonardo.backward(10)


# TODO 3: A to turn counter-clockwise
def counter_clockwise():
    leonardo.left(10)


# TODO 4: D to turn clockwise
def clockwise():
    leonardo.right(10)


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=counter_clockwise)
screen.onkey(key="d", fun=clockwise)

# TODO 5: C to clear drawing and comeback to origin
screen.onkey(key="c", fun=turtle_module.resetscreen)

# TODO 6: maintain the screen without disappearing while drawing
# TODO 7: turn off the game
screen.exitonclick()
