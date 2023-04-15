
# TODO modify the add function to take an unlimited number of arguments.
#  Use a loop to sum all the arguments inside the function.
#  Test it out by calling add() to calculate sum of some arguments.

def add(*args):
    print(args)
    addition = 0
    for number in args:
        print(f"here is the number: {number}")
        addition += number
    return addition


is_adding_numbers = 1
numbers = []
while is_adding_numbers:
    number = input("Please enter a number to add: ")
    if number == "n":
        is_adding_numbers = 0
    else:
        numbers.append(int(number))

numbers_t = tuple(numbers)
print(f"what the hell? {numbers_t}")
print(type(numbers_t))
print(add(3, 5, 6, 60, -87, 9, 123))



# TODO arguments with default values
# declare them with keyword arguments with a value
def my_function(a=1, b=2, c=3):
    # Do this with a
    # Then, Do this with b
    # Finally, Do this with c
    pass

# if later we call it with a value b = 2, this means that
# the b will be equal to 2 and a and b will be equal to their
# default values


# TODO unlimited positional arguments
# declare the function with an * before a name for the arguments
# that will be grouped into a TUPLE.
def add(*args):
    for n in args:
        print(n)


# TODO unlimited keyword arguments
# declare the function with an * before a name for the arguments
# that will be grouped into a dictionary.
def calculate(n, **kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(key)
        print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]


calculate(3, add=4, multiply=5)


class Car:

    def __init__(self, **kwargs):
        # self.make = kwargs["make"]  # bad way to get value from dict in class
        self.make = kwargs.get("make")  # good way
        self.model = kwargs.get("model")
        self.year = kwargs.get("year")


car = Car()

