import another_module
from turtle import Turtle, Screen

print(another_module.another_variable)

# here is happening the same we did above
# we are importing from another class


timmy = Turtle()  # how to create a new object from a blueprint
print(timmy)  # how to call a method that are associated with the object
timmy.shape("turtle")  # how to call a method that are associated with the object
timmy.color("blue", "coral")  # how to call a method that are associated with the object

my_screen = Screen()
print(my_screen)
print(my_screen.canvheight)  # how to tap into the objects attributes .canvheight for example
timmy.forward(100)
my_screen.exitonclick()
