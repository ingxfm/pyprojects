import turtle as t
from random import choice, randint
from time import sleep

juan_turtle = t.Turtle()
t.colormode(255)
juan_turtle.shape("turtle")
juan_turtle.color("navy", "coral")
screen = t.Screen()
juan_turtle.speed(0)

for sides in range(0, 36):
    r = randint(1, 254)  # / 255
    g = randint(1, 254)  # / 255
    b = randint(1, 254)  # / 255
    juan_turtle.pencolor(r, g, b)
    # juan_turtle.pensize(randint(2, 8))
    juan_turtle.circle(50)
    juan_turtle.left(10)


screen.exitonclick()
