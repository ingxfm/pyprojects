import turtle as t
from random import choice, randint
from time import sleep


juan_turtle = t.Turtle()
t.colormode(255)
juan_turtle.shape("turtle")
juan_turtle.color("navy", "coral")
screen = t.Screen()

juan_turtle.speed(0)

for sides in range(0, 250):
    r = randint(1, 254)  # / 255
    g = randint(1, 254)  # / 255
    b = randint(1, 254)  # / 255
    juan_turtle.pencolor(r, g, b)
    juan_turtle.pensize(randint(2, 8))
    if randint(1, 100) % 2 == 0:
        juan_turtle.forward(50)
    else:
        juan_turtle.back(50)
    if randint(1, 100) % 2 == 0:
        juan_turtle.right(90)
    else:
        juan_turtle.left(90)


screen.exitonclick()
