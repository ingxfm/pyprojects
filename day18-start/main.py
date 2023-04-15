import turtle as t
from random import randint


juan_turtle = t.Turtle()
t.colormode(255)
juan_turtle.shape("turtle")
juan_turtle.color("navy", "coral")

sides = 0
screen = t.Screen()
# while sides < 4:
#     juan_turtle.forward(100)
#     juan_turtle.right(90)
#     sides += 1
# juan_turtle.circle(35)
#
circle_angle = 360

for sides in range(3, 11):
    angle = circle_angle / sides
    r = randint(1, 254) #/ 255
    g = randint(1, 254) #/ 255
    b = randint(1, 254) #/ 255
    juan_turtle.pencolor(r, g, b)
    for _2 in range(sides):
        juan_turtle.forward(50)
        juan_turtle.right(angle)

# for _ in range(10):
#     juan_turtle.forward(10)
#     juan_turtle.penup()
#     juan_turtle.forward(10)
#     juan_turtle.pendown()



# juan_turtle.forward(100)
# juan_turtle.right(90)

# juan_turtle.forward(150)
screen.exitonclick()


# Tkinter = Tk interface to create GUIs in Python